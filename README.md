# Password Manager Written in Python

A simple local password manager written in Python and MariaDB. Uses [pbkdf2](https://en.wikipedia.org/wiki/PBKDF2) to derive a 256 bit key from a MASTER PASSWORD and DEVICE SECRET to use with AES-256 for encrypting/decrypting.


# Installation
You need to have python3 to run this on Windows, Linux or MacOS

## Windows
### Install Python Requirements
```pip install -r requirements.txt```

### MariaDB
#### Install
Follow [these instructions](https://www.mariadbtutorial.com/getting-started/install-mariadb/) to install MariaDB on Windows
#### Create user and grant privileges
- Navigate to MariaDB bin directory
```
C:\Program Files\MariaDB\bin
```
- Login as root with the password you chose while installation
```
mysql.exe -u root -p
```
- Create user
```
CREATE USER 'pm'@localhost IDENTIFIED BY 'password';
```
- Grant privileges
```
GRANT ALL PRIVILEGES ON *.* TO 'pm'@localhost IDENTIFIED BY 'password';
```


## Run/Usage
### Configure

You need to first configure the password manager by choosing a MASTER PASSWORD. This config step is only required to be executed once.
```
python config.py make
```
The above command will make a new configuration by asking you to choose a MASTER PASSWORD.
This will generate the DEVICE SECRET, create db and required tables.

```
python config.py delete
```
The above command will delete the existing configuration. Doing this will completely delete your device secret and all your entries and you will loose all your passwords. So be aware!

```
python config.py remake
```
The above command will first delete the existing configuration and create a fresh new configuration by asking you to choose a MASTER PASSWORD, generate the DEVICE SECRET, create the db and required tables.

### Usage
```
python pm.py -h

you can run this command for the help or more better understanding
```

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
