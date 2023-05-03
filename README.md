# Password Management Platform

A Python-based Password Manager has been developed, which provides a secure way to store and manage passwords while considering the following items:
Use a strong encryption algorithm for the passwords (the user's passwords are encrypted using AES-256)
Utilize master password for authorization/authentication
Allow users to add, retrieve, and generate passwords using a command-line interface
Include a password strength checker 
Implement logging to track activities  
We also used the MariaDB as the database. 


# Usage
## Requirements
•	Python 3.x
•	MariaDB 10.x
•	mysql-connector-python-8.0.33
•	pyperclip-1.8.2
•	pycryptodome-3.17

### MariaDB
#### Install
Follow [these instructions](https://www.mariadbtutorial.com/getting-started/install-mariadb/) to install MariaDB on Windows

#### Create user and necessary adjustments
Navigate to MariaDB bin directory in the machine
Login as root with the password you chose while installation
mysql.exe -u root -p

Create user
CREATE USER 'pm'@localhost IDENTIFIED BY 'password';

Grant privileges
GRANT ALL PRIVILEGES ON *.* TO 'pm'@localhost IDENTIFIED BY 'password';



## Run the code

### Installations
•	import dbconfig
•	pip install pycryptodome 
•	pip install pyperclip
•	pip install mysql-connector-python
--------------------------

### Configure
1-The first step is to initiate the code and set up a master password. To this end, use the following command:

python config.py make (the interface asks for the masterpassword)

This command will create a new configuration, generate the DEVICE SECRET, and create db and required tables.

2- The other command is to delete the existing configuration. All tables will also be deleted 

python config.py delete

3- And finally we can use "remake" to first delete the existing configuration and create a fresh new configuration by asking a new MASTER PASSWORD.

python config.py remake

4- To ask help, use 

python pm.py -h
-------------------------------

### Add entry
```
python pm.py add -s mysite -u mysite.com -e hello@email.com -l myusername
```
### Retrieve entry
```
python pm.py extract
```
The above command retrieves all the entries
```
python pm.py e -s mysite
```
The above command retrieves all the entries whose site name is "mysite"
```
python pm.py e -s mysite -l myusername
```
The above command retrieves the entry whose site name is "mysite" and username is "myusername"
```
python pm.py e -s mysite -l myusername --copy
```
The above command copies the password of the site "mysite" and username "myusername" into the clipboard
### Generate Password
```
python pm.py g --length 15
```
The above command generates a password of length 15 and copies to clipboard
