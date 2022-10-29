#!/usr/bin/python3

"""

@author    : Arslan Ahmad
VERSION_NUMBER = 1

"""

import os

def main():
    path = os.path.expanduser('~/.bashrc')
    pwd = os.getcwd()
    file = open(path, "a")
    file.write("\nalias pcs='/usr/bin/python3 " + pwd + "/pcs_commands.py'")
    file.write("\nalias sos='/usr/bin/python3 " + pwd + "/lvm_commands.py'")
    file.close()
    os.system('source ' + path)
    print("File updated.")

if __name__ == "__main__":
    main()
