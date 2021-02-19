import ftplib
import argparse

parser = argparse.ArgumentParser(description='Enter Host IP Address')
parser.add_argument('host', help='IP Address of the host')
args = parser.parse_args()
input_target = args.target
target = input_target


welcome_messgae = "Welcome to anonymous FTP login"

def anonlogin(hostname):
    try:
        ftp = ftplib.FTP(hostname)
        ftp.login()
        ftp.quit
        print(f"FTP Anonymous Logon Succeeded For Host: {hostname}")
        return True
    except:
        print(f"FTP Anonymous Logon Failed For Host: {hostname}")
        return False


anonlogin(target)
