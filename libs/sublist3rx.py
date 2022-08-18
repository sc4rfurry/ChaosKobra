#!/usr/bin/python3
import sublist3r



def scanner(target, filename):
    sublist3r.main(target, 60, filename, ports=None, silent=True, verbose=False, enable_bruteforce=False, engines=None)
