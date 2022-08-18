#!/use/bin/python3

from sys import argv, exit
from time import sleep
from subprocess import check_output
from os import getuid
from shlex import split as sp
from shutil import which




class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'





def banner():
    banner = f'''
            {bcolors.FAIL}──▄────▄▄▄▄▄▄▄────▄───
            ─▀▀▄─▄█████████▄─▄▀▀──
            ─────██─▀███▀─██──────
            ───▄─▀████▀████▀─▄────
            ─▀█────██▀█▀██────█▀──{bcolors.ENDC}
                            
        {bcolors.OKBLUE}──▄──▄────▄▀        ─▄▀▀███═◯
        ───▀▄─█─▄▀▄▄▄       ▐▌▄▀▀█▀▀▄
        ▄██▄████▄██▄▀█▄     █▐▌─────▐▌
        ─▀▀─█▀█▀▄▀███▀      █▐█▄───▄█▌
        ──▄▄▀─█──▀▄▄        ▀─▀██▄██▀{bcolors.ENDC}            
            
    {bcolors.OKCYAN}ChaosKobra{bcolors.ENDC} - {bcolors.OKBLUE}Just another Subdomain Enumeration Tool.{bcolors.ENDC}                
    '''
    print(banner)
    print("-" * 60 + "\n")



def done():
    print( bcolors.UNDERLINE + "\n\tEverything Installed Successfully..." + bcolors.ENDC)



def httpx():
    path = "src/"
    htpxt = which("httpxt")
    print(bcolors.OKCYAN + "\n\t\t[+] " + bcolors.ENDC + bcolors.BOLD + "Httpx" + bcolors.ENDC)
    if htpxt is not None:
        print(bcolors.OKGREEN + "\t\t   ==> Httpx Installed" + bcolors.ENDC)
        pass
    else:
        print(bcolors.OKBLUE + "\t\t   ==> " + bcolors.ENDC + bcolors.OKCYAN + "Initiating Installation Process..." + bcolors.ENDC)
        _golang = which("go")
        if _golang is not None:
            try:
                cmd = f"/usr/bin/chmod +x {path}httpx.sh"
                cmd = sp(cmd)
                check_output(cmd)
                cmd = f"/usr/bin/bash {path}httpx.sh > /dev/null 2>&1"
                cmd = sp(cmd)
                out = check_output(cmd)
                print(bcolors.OKGREEN + "\t\t   ==> Httpx Installed" + bcolors.ENDC)
            except Exception as err:
                print(bcolors.FAIL + "%s" %err + bcolors.ENDC)
                exit() 
        else:
            print(bcolors.WARNING + "\t\t[!] Golang is not installed..." + bcolors.ENDC)
            exit()



def httprobe():
    path = "src/"
    htprobe = which("httprobe")
    print(bcolors.OKCYAN + "\n\t\t[+] " + bcolors.ENDC + bcolors.BOLD + "Httprobe" + bcolors.ENDC)
    if htprobe is not None:
        print(bcolors.OKGREEN + "\t\t   ==> Httprobe Installed" + bcolors.ENDC)
        pass
    else:
        print(bcolors.OKBLUE + "\t\t   ==> " + bcolors.ENDC + bcolors.OKCYAN + "Initiating Installation Process..." + bcolors.ENDC)
        _golang = which("go")
        if _golang is not None:
            try:
                cmd = f"/usr/bin/chmod +x {path}httprobe.sh"
                cmd = sp(cmd)
                check_output(cmd)
                cmd = f"/usr/bin/bash {path}httprobe.sh > /dev/null 2>&1"
                cmd = sp(cmd)
                out = check_output(cmd)
                print(bcolors.OKGREEN + "\t\t   ==> Httprobe Installed" + bcolors.ENDC)
            except Exception as err:
                print(bcolors.FAIL + "%s" %err + bcolors.ENDC)
                exit() 
        else:
            print(bcolors.WARNING + "\t\t[!] Golang is not installed..." + bcolors.ENDC)
            exit()





def subFinder():
    path = "src/"
    sbfinder = which("subfinder")
    print(bcolors.OKCYAN + "\n\t\t[+] " + bcolors.ENDC + bcolors.BOLD + "Subfinder" + bcolors.ENDC)
    if sbfinder is not None:
        print(bcolors.OKGREEN + "\t\t   ==> Subfinder Installed" + bcolors.ENDC)
        pass
    else:
        _golang = which("go")
        print(bcolors.OKBLUE + "\t\t   ==> " + bcolors.ENDC + bcolors.OKCYAN + "Initiating Installation Process..." + bcolors.ENDC)
        if _golang is not None:
            try:
                cmd = f"/usr/bin/chmod +x {path}subfinder.sh"
                cmd = sp(cmd)
                check_output(cmd)
                cmd = f"/usr/bin/bash {path}subfinder.sh > /dev/null 2>&1"
                cmd = sp(cmd)
                check_output(cmd)
                print(bcolors.OKGREEN + "\t\t   ==> Subfinder Installed" + bcolors.ENDC)
            except Exception as err:
                print(bcolors.FAIL + "%s" %err + bcolors.ENDC)
                exit() 
        else:
            print(bcolors.WARNING + "\t\t[!] Golang is not installed..." + bcolors.ENDC)
            exit()



def check_user():
    banner()
    if getuid() == 0:
        print(bcolors.OKGREEN + "\t[#] " + bcolors.ENDC + bcolors.HEADER + f"{bcolors.OKGREEN}{argv[0]}{bcolors.ENDC} is Running as root." + bcolors.ENDC)
    else:
        exit(bcolors.OKGREEN + "\t[#] " + bcolors.ENDC + bcolors.HEADER + "You are not running as root." + bcolors.ENDC)



def main():
    print(bcolors.OKGREEN + "\t[#] " + bcolors.ENDC + bcolors.HEADER + "Setup is in process." + bcolors.ENDC)
    sleep(1)
    print(bcolors.OKGREEN + "\t[#] " + bcolors.ENDC + bcolors.HEADER + "Gethering up Tools." + bcolors.ENDC)
    sleep(2)
    subFinder()
    httprobe()
    httpx()
    done()

if __name__ == '__main__':
    check_user()
    main()
