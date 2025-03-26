# main.py

from user import User
from cmdtools import CmdTools

def main():
    name = input("What's your name? ")
    user = User(name)
    cmdtools = CmdTools(user)
    cmdtools.run()

if __name__ == "__main__":
    main()
