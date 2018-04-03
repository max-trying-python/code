import time
import getpass
import os
import sys


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


time.sleep(1)

hasResized = False
state = "start"

user = getpass.getuser()


def lockComputer():
    time.sleep(0.75)
    os.system("rundll32.exe user32.dll,LockWorkStation")


def clearScreen():
    os.system("cls")


def main():
    print(bcolors.HEADER + """
 _______  ______            _______  _       _________          _______  _______     _________ _______    _______          _________  _________          _______  _______  _______
(  ___  )(  __  \ |\     /|(  ____ \( (    /|\__   __/|\     /|(  ____ )(  ____ \    \__   __/(  ____ \    (  ___  )|\     /|\__   __/  \__   __/|\     /|(  ____ \(  ____ )(  ____ \\
| (   ) || (  \  )| )   ( || (    \/|  \  ( |   ) (   | )   ( || (    )|| (    \/       ) (   | (    \/    | (   ) || )   ( |   ) (        ) (   | )   ( || (    \/| (    )|| (    \/
| (___) || |   ) || |   | || (__    |   \ | |   | |   | |   | || (____)|| (__           | |   | (_____     | |   | || |   | |   | |        | |   | (___) || (__    | (____)|| (__
|  ___  || |   | |( (   ) )|  __)   | (\ \) |   | |   | |   | ||     __)|  __)          | |   (_____  )    | |   | || |   | |   | |        | |   |  ___  ||  __)   |     __)|  __)
| (   ) || |   ) | \ \_/ / | (      | | \   |   | |   | |   | || (\ (   | (             | |         ) |    | |   | || |   | |   | |        | |   | (   ) || (      | (\ (   | (
| )   ( || (__/  )  \   /  | (____/\| )  \  |   | |   | (___) || ) \ \__| (____/\    ___) (___/\____) |    | (___) || (___) |   | |        | |   | )   ( || (____/\| ) \ \__| (____/\\
|/     \|(______/    \_/   (_______/|/    )_)   )_(   (_______)|/   \__/(_______/    \_______/\_______)    (_______)(_______)   )_(        )_(   |/     \|(_______/|/   \__/(_______/
""" + bcolors.ENDC + """

Press F11 & unplug your mouse for best gameplay
Press enter to continue
""")

    input()

    print("""
Hello, {}!
Your name sounds like a nerd. Good. This is a code-golf adventure. Have fun.
""".format(user))

    time.sleep(0.5)
    clearScreen()

    print("""Challenge number 1
Bash: remove every file, directory, simlink, etc that can be removed by root. Assume that your code is being run by a non-root user that is in the sudoers file.
""")

    rmRf = input(user + "@localhost:~$ ")

    if rmRf == "sudo rm -rf --no-preserve-root /":
        print("Nice, but not very golfed. You have tried. But you did not succeede. Prepare for shutdown.")
        os.system("shutdown /s /t 15")
        time.sleep(2.5)
        print("Just kidding. I trolled you.")
        os.system("shutdown /a")
    elif rmRf == "rm -rf --no-preserve-root /":
        print("You forgot to run as root.")
        print("""
 ▄█        ▄██████▄   ▄████████    ▄█   ▄█▄  ▄█  ███▄▄▄▄      ▄██████▄        ▄████████  ▄██████▄     ▄▄▄▄███▄▄▄▄      ▄███████▄ ███    █▄      ███        ▄████████    ▄████████
███       ███    ███ ███    ███   ███ ▄███▀ ███  ███▀▀▀██▄   ███    ███      ███    ███ ███    ███  ▄██▀▀▀███▀▀▀██▄   ███    ███ ███    ███ ▀█████████▄   ███    ███   ███    ███
███       ███    ███ ███    █▀    ███▐██▀   ███▌ ███   ███   ███    █▀       ███    █▀  ███    ███  ███   ███   ███   ███    ███ ███    ███    ▀███▀▀██   ███    █▀    ███    ███
 ███       ███    ███ ███         ▄█████▀    ███▌ ███   ███  ▄███             ███        ███    ███  ███   ███   ███   ███    ███ ███    ███     ███   ▀  ▄███▄▄▄      ▄███▄▄▄▄██▀
███       ███    ███ ███        ▀▀█████▄    ███▌ ███   ███ ▀▀███ ████▄       ███        ███    ███  ███   ███   ███ ▀█████████▀  ███    ███     ███     ▀▀███▀▀▀     ▀▀███▀▀▀▀▀
███       ███    ███ ███    █▄    ███▐██▄   ███  ███   ███   ███    ███      ███    █▄  ███    ███  ███   ███   ███   ███        ███    ███     ███       ███    █▄  ▀███████████
 ███▌    ▄ ███    ███ ███    ███   ███ ▀███▄ ███  ███   ███   ███    ███      ███    ███ ███    ███  ███   ███   ███   ███        ███    ███     ███       ███    ███   ███    ███
█████▄▄██  ▀██████▀  ████████▀    ███   ▀█▀ █▀    ▀█   █▀    ████████▀       ████████▀   ▀██████▀    ▀█   ███   █▀   ▄████▀      ████████▀     ▄████▀     ██████████   ███    ███
▀                                 ▀                                                                                                                                    ███    ███
 """)
        lockComputer()
        clearScreen()
        print("I guess you know the password. You are a")
        print("""
    ▄█    █▄       ▄████████  ▄████████    ▄█   ▄█▄    ▄████████    ▄████████
  ███    ███     ███    ███ ███    ███   ███ ▄███▀   ███    ███   ███    ███
  ███    ███     ███    ███ ███    █▀    ███▐██▀     ███    █▀    ███    ███
  ▄███▄▄▄▄███▄▄   ███    ███ ███         ▄█████▀     ▄███▄▄▄      ▄███▄▄▄▄██▀
▀▀███▀▀▀▀███▀  ▀███████████ ███        ▀▀█████▄    ▀▀███▀▀▀     ▀▀███▀▀▀▀▀
  ███    ███     ███    ███ ███    █▄    ███▐██▄     ███    █▄  ▀███████████
   ███    ███     ███    ███ ███    ███   ███ ▀███▄   ███    ███   ███    ███
  ███    █▀      ███    █▀  ████████▀    ███   ▀█▀   ██████████   ███    ███
                                         ▀                        ███    ███
                                         """)
    elif rmRf == "":
        print("You are too lazy. Prepare for HIBERNATION!")
        time.sleep(1.5)
        os.system("shutdown /h /f")
        time.sleep(1)
        sys.exit()
    else:
        print(rmRf)


main()
