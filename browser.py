#!/usr/bin/python
#TGWIL
import os
import time
import apt
def main():
    os.system("clear")
    os.system("figlet MUTI")
    print("Select a fucking thing\n\t1) Browsers\n\t2) Pre-Install for tools")
    inp=int(input(">>>"))
    if inp==1:
        browser()
    elif inp==2:
        installt()


def installt():
    print("CHECKING PACKAGES")
    time.sleep(1)
    os.system("apt update -y")
    cache = apt.Cache()
    if cache['git'].is_installed:
        print("Git OK>>>")
    else:
        print("Git is not installed, INSTALLING GIT")
        os.system("xterm \"☣ INSTALL GIT ☣\" -geometry 100x30 -e  \"sudo apt-get install git -y" )
    if cache['python-pip'].is_installed:
        print("Python3  OK>>>")
    else:
        print("Pip is not installed, INSTALLING PIP")
        os.system("xterm -T \"☣ INSTALL PIP ☣\" -geometry 100x30 -e  \"sudo apt-get install python-pip -y")
    if cache['curl'].is_installed:
        print("Curl OK>>>")
    else:
        print("Curl is not installed, INSTALLING CURL")
        os.system("xterm -T \"☣ INSTALL CURL ☣\" -geometry 100x30 -e  \"sudo apt-get install -y")
    time.sleep(5)
    browser()

def browser():
    os.system("clear")
    os.system("figlet MUTI")
    print("Choose a browser>>>\n\t1) Brave browser\n\t2) Tor Browser\n\t3) Firefox-esr")
    browinp=int(input(">>>>"))
    if browinp==1:
        os.system("curl -fsSLo /usr/share/keyrings/brave-browser-archive-keyring.gpg https://brave-browser-apt-release.s3.brave.com/brave-browser-archive-keyring.gpg&&echo \"deb [signed-by=/usr/share/keyrings/brave-browser-archive-keyring.gpg] https://brave-browser-apt-release.s3.brave.com/ stable main\"|sudo tee /etc/apt/sources.list.d/brave-browser-release.list&&apt update&&apt install brave-browser")
    elif browinp==2:
        os.system("apt-get install torbrowser_launcher")
    elif browinp==3:
        os.system("apt-get install firefox-esr")

main()

