import os
import apt
def apttools():
    os.system("apt update -y")
    cache = apt.Cache()
    if cache['zaproxy'].is_installed:
        print("Owasp Zap ✓>>>")
    else:
        print("Zap is not installed, INSTALLING ZAP")
        os.system("xterm -T \"☣ INSTALL ZAP-PROXY ☣\" -geometry 100x30 -e  \"sudo apt-get install zaproxy -y")
    if cache['instaloader'].is_installed:
        print("instaloader ✓>>>")
    else:
        print("Instaloader is not installed, INSTALLING INSTALOADER")
        os.system("xterm -T \"☣ INSTALL INSTALOADER ☣\" -geometry 100x30 -e  \"sudo apt-get install instaloader -y")
    if cache['httrack'].is_installed:
        print("HTTRACK ✓>>>")
    else:
        print("Httrack is not installed, INSTALLING HTTRACK")
        os.system("xterm -T \"☣ INSTALL HTTRACK ☣\" -geometry 100x30 -e  \"sudo apt-get install httrack -y")
    if cache['bettercap'].is_installed:
        print("BetterCap ✓>>>")
    else:
        print("BetterCap is not installed, INSTALLING BETTERCAP")
        os.system("xterm -T \"☣ INSTALL BETTERCAP ☣\" -geometry 100x30 -e  \"sudo apt-get install bettercap -y")

def all():
    os.system("git clone https://github.com/screetsec/TheFatRat.git")
    path = os.getcwd()+'/TheFatRat'
    varmi = os.path.exists(path)
    if varmi==True:
        os.system("git clone https://github.com/1N3/Sn1per.git")
        path = os.getcwd()+'/Sn1per'
        varmi = os.path.exists(path)
        if varmi == True:
            os.system("git clone https://github.com/Manisso/fsociety.git")
            path = os.getcwd()+'/fsociety'
            varmi = os.path.exists(path)
            if varmi == True:
                print("Are you want to install apt tools??")
                zap=input(">>>(y/n)")
                if  zap == 'y' or zap == 'Y':
                    apttools()
                elif zap == 'n' or zap == 'N':
                    exit()
                return zap


            else:
                print("siktimin kodunda hata yaptın amk asalağı")

def main():
    os.system("clear")
    os.system("figlet MUTI")
    print("WARNING! THIS SCRIPT ONLY INSTALLS GIT REPO NOT THE DIRECTLY TOOL")
    print('Are you sure About installing useful tools from git?')
    userinp=input(">>>(y/n)")
    if userinp=='y' or userinp=='Y':
        all()
    elif userinp=='n' or userinp=='N':
        exit()
    return userinp
main()