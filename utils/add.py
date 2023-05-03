from utils.dbconfig import dbconfig
import utils.aesutil
from getpass import getpass
import re

import logging
logging.basicConfig(filename='password_manager.log', level=logging.DEBUG, format='%(asctime)s %(levelname)s:%(message)s')

from Crypto.Protocol.KDF import PBKDF2
from Crypto.Hash import SHA512
from Crypto.Random import get_random_bytes
import base64

from rich import print as printc
from rich.console import Console

def computeMasterKey(mp,ds):
	password = mp.encode()
	salt = ds.encode()
	key = PBKDF2(password, salt, 32, count=1000000, hmac_hash_module=SHA512)
	return key


def checkEntry(sitename, siteurl, email, username):
	db = dbconfig()
	cursor = db.cursor()
	query = f"SELECT * FROM pm.entries WHERE sitename = '{sitename}' AND siteurl = '{siteurl}' AND email = '{email}' AND username = '{username}'"
	cursor.execute(query)
	results = cursor.fetchall()

	if len(results)!=0:
		return True
	return False


def addEntry(mp, ds, sitename, siteurl, email, username):
	# Check if the entry already exists
	if checkEntry(sitename, siteurl, email, username):
		printc("[yellow][-][/yellow] Entry with these details already exists")
		logging.info('Details already exists, Duplicated entries can not be saved in the DataBase ')
		return

	# Input Password
	#password = getpass("Password: ")
	# while True:
	# 	password = getpass('Enter Password: ')
	# 	if validate_password(password):
	# 		break
	# 	else:
	# 		printc("[red][!] Password does not meet the criteria[/red]")

	while True:
		password = getpass('Enter Password: ')
		valid, message = validate_password(password)
		if valid:
			break
		else:
			printc(f"[red][!] {message}[/red]")

	# compute master key
	mk = computeMasterKey(mp,ds)

	# encrypt password with mk
	encrypted = utils.aesutil.encrypt(key=mk, source=password, keyType="bytes")

	# Add to db
	db = dbconfig()
	cursor = db.cursor()
	query = "INSERT INTO pm.entries (sitename, siteurl, email, username, password) values (%s, %s, %s, %s, %s)"
	val = (sitename,siteurl,email,username,encrypted)
	cursor.execute(query, val)
	db.commit()

	printc("[green][+][/green] Added entry ")
	logging.info('A new password entry has been made for the user ')



#Implementing password policies

def validate_password(password):
    if len(password) < 8:
        return False, "Password must be at least 8 characters long"
    logging.info("Can not add the entry because password should be 8 characters long")
    if not re.search("[a-z]", password):
        return False, "Password must contain at least one lowercase letter"
    logging.info("Can not add the entry because password should have atleast one lowercase letter")
    if not re.search("[A-Z]", password):
        return False, "Password must contain at least one uppercase letter"
    logging.info("Can not add the entry because password should have atleast one uppercase letter")
    if not re.search("[0-9]", password):
        return False, "Password must contain at least one digit"
    logging.info("Can not add the entry because password should have atleast one digit")
    if not re.search("[!@#$%^&*\\(\\)_=+{};:',<.>/?`~\\\\|-]", password):
        return False, "Password must contain at least one special character"
    logging.info("Can not add the entry because password should have atleast one special character")
    return True, "Password meets all requirements" 