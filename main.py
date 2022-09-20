#!/usr/bin/python3

from sys import argv
import sys
try:
    from libs import sublist3rx
except Exception as err:
    print(err)
    exit(1)
from os import path as pt
from os import makedirs, mkdir, system
from os import devnull as dnull
from threading import Thread
from time import sleep
from contextlib import contextmanager
from os import popen as pop


global_domain = ""


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




@contextmanager
def suppress_stdout():
    with open(dnull, "w") as devnull:
        old_stdout = sys.stdout
        sys.stdout = devnull
        try:  
            yield
        finally:
            sys.stdout = old_stdout




def banner():
    banner = f"""
                                {bcolors.FAIL}──▄────▄▄▄▄▄▄▄────▄─── 
                                ─▀▀▄─▄█████████▄─▄▀▀──                      
                                ─────██─▀███▀─██──────
                                ───▄─▀████▀████▀─▄────
                                ─▀█────██▀█▀██────█▀──{bcolors.ENDC}
        _________ .__                           ____  __.    ___.                 
        \_   ___ \|  |__ _____    ____  ______ |    |/ _|____\_ |______________   
        /    \  \/|  |  \\__  \  /  _ \/  ___/ |      < /  _ \| __ \_  __ \__  \  
        \     \___|   Y  \/ __ \(  <_> )___ \  |    |  (  <_> ) \_\ \  | \// __ \_
        \______  /___|  (____  /\____/____  > |____|__ \____/|___  /__|  (____  /
                \/     \/     \/           \/          \/         \/           \/ 
    
    {bcolors.OKCYAN}\t\tChaosKobra{bcolors.ENDC} - {bcolors.OKBLUE}Just another Subdomain Enumeration Tool.{bcolors.ENDC}                
    """
    print(banner)
    print("-" * 90 + "\n")


def help():
    help = f'''
        {bcolors.OKCYAN}>> Help for ChaosKobra{bcolors.ENDC}
        
        {bcolors.FAIL}usage:{bcolors.ENDC} python3 {argv[0]} -t [domain] -o (Output File)

            {bcolors.BOLD}Options:{bcolors.ENDC}
                -t              Target or Host
                -o              Output Folder (Optional)
        
        {bcolors.OKGREEN}examples:{bcolors.ENDC} 
            1) python3 main.py -t example.com
            2) python3 main.py -t example.com -o example
    '''
    print(help)
    exit(1)



def url_handler(host):
    global domain
    if host[:8] == "https://" or host[:7] == "http://":
        domain = str(host).split("://")[1].split("/")[0]
        return domain
    else:
        domain = str(host)
        return domain




def get_subfinder(global_domain, sbfinder):
    # subfinder -d domain.com -o output.txt -silent
    print(f"{bcolors.OKGREEN}[+]{bcolors.ENDC} {bcolors.OKBLUE}[info]{bcolors.ENDC} {bcolors.BOLD}{bcolors.OKGREEN}SubFinder{bcolors.ENDC}")
    global out_file_sbfinder
    out_file_sbfinder = sbfinder + '/' + "all_domains.log" 
    cmd = f"subfinder -d {global_domain} -o {out_file_sbfinder} -silent > /dev/null 2>&1"
    system(cmd)
    if pt.exists(out_file_sbfinder) and pt.isfile(out_file_sbfinder):
        with open(out_file_sbfinder, "r") as handle:
            reader = handle.readlines()
            if len(reader) != 0:
                for sub in reader:
                    print(f"{bcolors.OKCYAN}[Sub-Domain]{bcolors.ENDC} " + str(sub).strip("\n"))
            else:
                print(f"{bcolors.WARNING}[!]{bcolors.ENDC} {len(reader)} Sub-Domains Found.")
        handle.close()
    else:
        print(f"{bcolors.WARNING}[!]{bcolors.ENDC} No Sub-Domains Found.")
        pass            
    return out_file_sbfinder


def tailem(subfile, thread):
    subfile.seek(0, 2)
    while thread.is_alive():
        line = subfile.readline()
        if not line:
            sleep(0.1)
            continue
        yield line
    else:
        pass



def amass_domains(out_file_amassx, t_amass):
    try:
        sleep(10)
        if pt.exists(out_file_amassx):
            print(f"{bcolors.WARNING}[!]{bcolors.ENDC} This will take some time.")
        else:
            pass
        while not pt.exists(out_file_amassx):

            sleep(5)
        else:
            if pt.exists(out_file_amassx) and pt.isfile(out_file_amassx):
                subfile = open(out_file_amassx, "r")
                tailit = tailem(subfile, t_amass)
                for sub in tailit:
                    print(f"{bcolors.OKCYAN}[Sub-Domain]{bcolors.ENDC} " + str(sub).strip("\n"))
            else:
                print(f"{bcolors.WARNING}[!]{bcolors.ENDC} No Sub-Domains Found.")
                pass
    except Exception as err:
        print(err)
        exit(1)




def get_amass(global_domain, out_file_amassx):
    # amass enum -d domain --active -o path -r 8.8.8.8,1.1.1.1,208.67.222.222,8.26.56.26,9.9.9.9,64.6.65.6,13.239.157.177,91.239.100.100
    print(f"{bcolors.OKGREEN}[+]{bcolors.ENDC} {bcolors.OKBLUE}[info]{bcolors.ENDC} {bcolors.BOLD}{bcolors.OKGREEN}Amass{bcolors.ENDC}")
    cmd = f"amass enum -d {global_domain} --active -o {out_file_amassx} -r 8.8.8.8,1.1.1.1 > /dev/null 2>&1"
    system(cmd)
    


def amass_thread(global_domain, amassx):
    global out_file_amassx
    out_file_amassx = amassx + '/' + "all_domains.log"
    t_ammas = Thread(target=get_amass, args=(global_domain, out_file_amassx))
    try:
        t_ammas.start()
        amass_domains(out_file_amassx, t_ammas)
        t_ammas.join()
    except KeyboardInterrupt:
        print("\n")
        pass
    
    return out_file_amassx


def get_sublister(global_domain, sblist3r):
    print(f"{bcolors.OKGREEN}[+]{bcolors.ENDC} {bcolors.OKBLUE}[info]{bcolors.ENDC} {bcolors.BOLD}{bcolors.OKGREEN}Sublist3r{bcolors.ENDC}")
    global out_file_sblist3r
    out_file_sblist3r = sblist3r + '/' + "all_domains.log"
    try:
        with suppress_stdout():
            sublist3rx.scanner(global_domain, out_file_sblist3r)
        if pt.exists(out_file_sblist3r) and pt.isfile(out_file_sblist3r):
            with open(out_file_sblist3r, "r") as handle:
                reader = handle.readlines()
                if len(reader) != 0:
                    for sub in reader:
                        print(f"{bcolors.OKCYAN}[Sub-Domain]{bcolors.ENDC} " + str(sub).strip("\n"))
                else:
                    print(f"{bcolors.WARNING}[!]{bcolors.ENDC} {len(reader)} Sub-Domains Found.")
            handle.close()
        else:
            print(f"{bcolors.WARNING}[!]{bcolors.ENDC} No Sub-Domains Found.")
            pass
    except Exception as err:
        print(err)
        exit(1)
    return out_file_sblist3r


def get_domains(_root_folder, out_file_sbfinder, out_file_amassx, out_file_sblist3r):
    global domains_out
    domains_out = _root_folder + "sub_domains.log"
    all_domains = []
    final_domain_list = []
    print(f"{bcolors.OKGREEN}[+]{bcolors.ENDC} {bcolors.OKBLUE}[info]{bcolors.ENDC} {bcolors.BOLD}{bcolors.OKGREEN}Gathering all Sub-Domains...{bcolors.ENDC}")
    try:
        if pt.exists(out_file_sbfinder) and pt.isfile(out_file_sbfinder):
            with open(out_file_sbfinder, "r") as handle:
                reader = handle.readlines()
                for url in reader:
                    all_domains.append(str(url).strip("\n"))
            handle.close()
        else:
            pass
        if pt.exists(out_file_amassx) and pt.isfile(out_file_amassx):
            with open(out_file_amassx, "r") as handle:
                reader = handle.readlines()
                for url in reader:
                    all_domains.append(str(url).strip("\n"))
            handle.close()
        else:
            pass
        if pt.exists(out_file_sblist3r) and pt.isfile(out_file_sblist3r):
            with open(out_file_sblist3r, "r") as handle:
                reader = handle.readlines()
                for url in reader:
                    all_domains.append(str(url).strip("\n"))
            handle.close()
        else:
            pass

        for _ in all_domains:
            if _ not in final_domain_list:
                final_domain_list.append(_)
        
        with open(domains_out, "a+") as handle:
            for host in final_domain_list:
                handle.write(host + "\n") 
        handle.close()
        print(f"{bcolors.OKGREEN}[+] Done{bcolors.ENDC}")
        return domains_out
    except Exception as err:
        print(err)
        exit(1)



def get_httprobe(domains_out):
    global httprobe_out
    print(f"{bcolors.OKGREEN}[+]{bcolors.ENDC} {bcolors.OKBLUE}[info]{bcolors.ENDC} {bcolors.BOLD}{bcolors.OKGREEN}Probing for http/https{bcolors.ENDC}")
    httprobe_out = _root_folder + "valid_sub-domains.log"
    try:
        cmd = f"cat {domains_out} | httprobe | tee -a {httprobe_out} > /dev/null 2>&1"
        system(cmd)
        if pt.exists(httprobe_out) and pt.isfile(httprobe_out):
            with open(httprobe_out, "r") as handle:
                reader = handle.readlines()
                if len(reader) != 0:
                    for sub in reader:
                        print(f"{bcolors.OKCYAN}[Sub-Domain]{bcolors.ENDC} {bcolors.OKBLUE}[Alive] {bcolors.ENDC}" + str(sub).strip("\n"))
                else:
                    print(f"{bcolors.WARNING}[!]{bcolors.ENDC} {len(reader)} Sub-Domains Alive.")
                    exit(1)
            handle.close()
    except Exception as err:
        print(err)
        exit(1)


def save_httpx(httpx_out, url, _title, _ip, _method, _status_code, _web_server, _tech, _follow_red):
    try:
        with open(httpx_out, "a+") as handle:
            handle.write(url + "\n")
            handle.write("\tTitle: " + _title + "\n")
            handle.write("\tIP: " + _ip + "\n")
            handle.write("\tMethod: " + _method + "\n")
            handle.write("\tStatus Code: " + _status_code + "\n")
            handle.write("\tWeb Server: " + _web_server + "\n")
            handle.write("\tWeb Tech: " + _tech + "\n")
            handle.write("\tRedirect(s) " + _follow_red + "\n")
            handle.write("-" * 70 + "\n")
        handle.close()
    except Exception as err:
        print(err)
        exit(1)


def get_httpx(httprobe_out):
    # httpx -title -tech-detect -status-code -cdn -follow-redirects -ip -method -web-server
    global httpx_out
    sub_domains_list = []
    _title = "None"
    _ip = "None"
    _method = "None"
    _status_code = "None"
    _web_server = "None"
    _tech = "None"
    _follow_red = "None"
    print(f"{bcolors.OKGREEN}[+]{bcolors.ENDC} {bcolors.OKBLUE}[info]{bcolors.ENDC} {bcolors.BOLD}{bcolors.OKGREEN}Analyzing Sub-Domains.{bcolors.ENDC}")
    httpx_out = _root_folder + "httpx_sub-domains.log"
    try:
        with open(httprobe_out, "r") as handle:
            reader = handle.readlines()
        handle.close()
        for sub in reader:
            sub_domains_list.append(str(sub).strip("\n"))
        for url in sub_domains_list:
            print(f"{bcolors.OKCYAN}[Sub-Domain]{bcolors.ENDC} {bcolors.OKGREEN}[Analyzer] {bcolors.ENDC}" + str(url).strip("\n"))
            _title = pop(f'echo "{url}" | httpxt -title -silent -no-color').read()
            print(f"\t{bcolors.HEADER}[-]{bcolors.ENDC} Title:\t" + f"{bcolors.FAIL}" + " ".join(_title.split(" ")[1:]).strip("\n")[1:-1] + f"{bcolors.ENDC}")
            _ip = pop(f'echo "{url}" | httpxt -ip -silent').read()
            print(f"\t{bcolors.HEADER}[-]{bcolors.ENDC} IP:\t\t" + f"{bcolors.FAIL}" + " ".join(_ip.split(" ")[1:]).strip("\n")[1:-1] + f"{bcolors.ENDC}")
            _method = pop(f'echo "{url}" | httpxt -method -silent -no-color').read()
            print(f"\t{bcolors.HEADER}[-]{bcolors.ENDC} Method:\t" + f"{bcolors.FAIL}" + " ".join(_method.split(" ")[1:]).strip("\n")[1:-1] + f"{bcolors.ENDC}")
            _status_code = pop(f'echo "{url}" | httpxt -status-code -silent -no-color').read()
            print(f"\t{bcolors.HEADER}[-]{bcolors.ENDC} Status Code:\t" + f"{bcolors.FAIL}" + " ".join(_status_code.split(" ")[1:]).strip("\n")[1:-1] + f"{bcolors.ENDC}")
            _web_server = pop(f'echo "{url}" | httpxt -web-server -silent -no-color').read()
            print(f"\t{bcolors.HEADER}[-]{bcolors.ENDC} Web Server:\t" + f"{bcolors.FAIL}" + " ".join(_web_server.split(" ")[1:]).strip("\n")[1:-1] + f"{bcolors.ENDC}")
            _tech = pop(f'echo "{url}" | httpxt -tech-detect -silent -no-color').read()
            print(f"\t{bcolors.HEADER}[-]{bcolors.ENDC} Tech:\t" + f"{bcolors.FAIL}" + " ".join(_tech.split(" ")[1:]).strip("\n")[1:-1] + f"{bcolors.ENDC}")
            _follow_red = pop(f'echo "{url}" | httpxt -follow-redirects -silent -no-color').read()
            print(f"\t{bcolors.HEADER}[-]{bcolors.ENDC} Redirect(s):\t" + f"{bcolors.FAIL}" + " ".join(_follow_red.split(" ")[1:]).strip("\n")[1:-1] + f"{bcolors.ENDC}")
            save_httpx(httpx_out, url, _title, _ip, _method, _status_code, _web_server, _tech, _follow_red)
    except Exception as err:
        print(err)
        exit(1)



def folder_strct(results_dir, output):
    global _root_folder
    _root_folder = results_dir + output + "/"

    global sbfinder
    global amassx
    global sblist3r
    _folders = [
        "subfinder",
        "amass",
        "sublist3r"
    ]

    for every_folder in _folders:
        _path = _root_folder + every_folder
        if pt.exists(str(_path)) and pt.isdir(str(_path)):
            pass
        else:
            try:
                makedirs(_path)
            except Exception as err:
                print(err)
                exit(1)
    
    sbfinder = _root_folder + "subfinder"
    amassx = _root_folder + "amass"
    sblist3r = _root_folder + "sublist3r"
    return [sbfinder, amassx, sblist3r, _root_folder]




def _stdout():
    global results_dir
    results_dir = "Output/"
    if pt.exists(results_dir) and pt.isdir(results_dir):
        return results_dir
    else:
        try:
            mkdir(results_dir)
            return results_dir
        except Exception as err:
            print(err)
            exit(1)





def main(global_domain):
    global output

    if len(argv) < 2:
        help()
    elif len(argv) == 3:
        if argv[1] == "-t":
            host = str(argv[2])
            output = host
        else:
            print(f"{bcolors.FAIL}Argument missing. -t(Target){bcolors.ENDC}")
            help()
    elif len(argv) == 5:
        if argv[1] == "-t" and argv[3] == "-o":
            host = str(argv[2])
            output = str(argv[4])
        else:
            print(f"{bcolors.FAIL}Invalid Arguments...{bcolors.ENDC}")
            help()
    else:
        print(f"{bcolors.FAIL}Invalid Arguments...{bcolors.ENDC}")
        help()


    _stdout()
    url_handler(host)
    if len(argv) == 5 and argv[3] == "-o":
        folder_strct(results_dir, output)
    else:
        folder_strct(results_dir, domain)
    global_domain = domain
    print(f"{bcolors.OKBLUE}[info]{bcolors.ENDC} {bcolors.BOLD}{bcolors.OKCYAN}Subdomain Enumeration...{bcolors.ENDC}")
    get_subfinder(global_domain, sbfinder)
    amass_thread(global_domain, amassx)
    get_sublister(global_domain, sblist3r)
    print(f"\n{bcolors.OKBLUE}[info]{bcolors.ENDC} {bcolors.BOLD}{bcolors.OKCYAN}Analyzing Sub-Domians...{bcolors.ENDC}")
    get_domains(_root_folder, out_file_sbfinder, out_file_amassx, out_file_sblist3r)
    get_httprobe(domains_out)
    get_httpx(httprobe_out)





if __name__ == '__main__':
    banner()
    main(global_domain)