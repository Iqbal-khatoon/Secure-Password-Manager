# (1) Password Management Platform

A Python-based Password Manager has been developed, which provides a secure way to store and manage passwords while considering the following items:

Use a strong encryption algorithm for the passwords (the user's passwords are encrypted using AES-256)

Utilize master password for authorization/authentication

Allow users to add, retrieve, and generate passwords using a command-line interface

Include a password strength checker 

Implement logging to track activities  

We also used the MariaDB as the database. 


# (2) Usage
## (2-1) Requirements
Python 3.x

MariaDB 10.x

mysql-connector-python-8.0.33

pyperclip-1.8.2

pycryptodome-3.17

## (2-2) MariaDB

Follow [these instructions](https://www.mariadbtutorial.com/getting-started/install-mariadb/) to install MariaDB on Windows.

Navigate to MariaDB bin directory in the machine

Login as root with the password you chose while installation

mysql.exe -u root -p

Create user

CREATE USER 'pm'@localhost IDENTIFIED BY 'password';

Grant privileges

GRANT ALL PRIVILEGES ON *.* TO 'pm'@localhost IDENTIFIED BY 'password';



## (2-3) Run the code

### Installations

import dbconfig

pip install pycryptodome 

pip install pyperclip

pip install mysql-connector-python

### Configure

(i) The first step is to initiate the code and set up a master password. To this end, use the following command:

python config.py make (the interface asks for the masterpassword)

This command will create a new configuration, generate the DEVICE SECRET, and create db and required tables.

(ii) The other command is to delete the existing configuration. All tables will also be deleted 

python config.py delete

(iii) And finally we can use "remake" to first delete the existing configuration and create a fresh new configuration by asking a new MASTER PASSWORD.

python config.py remake

(iv) To ask help, use 

python pm.py -h

### Commands

(i) Add entry

To add a set of username and passords for each website use the following command. Note that, the utility asks for a password until the requirements are met (a loop) and encryption will be implemented immediately.

python pm.py add -s website-name -u website-url -e user-email -l username


(ii) Retrieve entry

The following command will be used to retrieve all usernames and websites from the datavase:

python pm.py extract

The following command will be used to retrieve all usernames for an specefic websites from the datavase:

python pm.py e -s website-name

(iii) Access password

The below command allow the user to copy the password of a specific website name and username into the clipboard:

python pm.py e -s website-name -l username --copy

(iv) Generate Password

This command generates a password of length xx and copies it to the clipboard

python pm.py g --length xx



# (3) Other Features of the code

Strong encryption/decryption algorithm for the passwords

Authentication techniques and using master passwords

Allows users to add, retrieve, and generate passwords using a command-line interface

The software also includes a password strength checker 

Logging to track activities  

Entry with these details already exists

