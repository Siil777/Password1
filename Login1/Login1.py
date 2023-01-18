from typing import Any
from module2 import*
import sys
import string
from re import*

while True:
        print("Write 1 for reg or 0 for exit")
        cmd = input()
        if cmd == '1':
            add_user=()
        elif cmd == '0': 
            sys.exit()
        else: print("Wrong command")

        while True:
                login = input("Enter login: ")
                passw = input("Enter password: ")
                if login not in logins:
                    print("Success.")
                    users[login] = passw
                    break
                else: print("There is a user with this username. Try again with other username.")


   
