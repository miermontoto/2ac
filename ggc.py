import sys
import os
from colorama import Fore, Style, init

init()

def warning(x):
    p = ""
    if(x == "noparm"): p = "at least one parameter is needed."
    elif(x == "badext"): p = "the target file has to have '.c' extension."
    elif(x == "failver"): p = "failed to verify." 
    else: p = "unrecognised error."
    print(Fore.LIGHTMAGENTA_EX + tag + Fore.RED + "ERROR: " + Fore.RESET + p)
    exit()

def redirect(x):
    global alert, cleanup, verify
    x = x[1:2:]
    if(x == 'w'): alert = True
    elif(x == 'o'): cleanup = False
    elif(x == 'v'): verify = True

def process(n):
    global alert, verify, cleanup, tag
    x = os.path.splitext(n)[0]
    if not os.path.splitext(n)[1] == ".c":
        warning("badext")
    print(Fore.LIGHTMAGENTA_EX + tag + Fore.BLUE + 
        "target file: " + Style.RESET_ALL + x)

    os.system("gcc -c " + x + ".c")
    os.system("gcc " + x + ".o -o " + x)
    if cleanup == True: os.system("rm " + x + ".o")
    print(Fore.LIGHTMAGENTA_EX + tag + Fore.GREEN +
          "completed all tasks." + Style.RESET_ALL)

    if verify == True: 
        if os.path.isfile(x) and not os.path.isfile(x + ".o"): 
            print(Fore.LIGHTMAGENTA_EX + tag +
                  Fore.YELLOW + "successfully verified.")
        else: warning("failver")

i = 1
verify = False
cleanup = True
alert = False
tag = "ggc.py "
print(Fore.LIGHTMAGENTA_EX + tag + Fore.RESET +
     "detected " + str(len(sys.argv) - 1) + " parameter(s).")
if(i == len(sys.argv)): warning("noparm")
while(i < len(sys.argv)):
    if(sys.argv[i][0:1:] == '-'): redirect(sys.argv[i])
    else: process(sys.argv[i])
    i += 1
