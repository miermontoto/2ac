from sys import argv
from os import system, path, truncate
from colorama import Fore, Style, init

reset = Fore.RESET # short reset to avoid lengty commands
init() # colorama is initiated

def warning(x): # only called if a error is detected
    p = ""
    if(x == "noparm"): p = "at least one parameter is needed."
    elif(x == "badext"): p = "the target file has to have '.c' extension."
    elif(x == "failver"): p = "failed to verify."
    else: p = "unrecognised error."
    print(tag + Fore.RED + "ERROR: " + reset + p)
    exit() # if an error is detected, the script should NOT continue compiling.

def help():
    print(tag)
    print(tag + Fore.LIGHTYELLOW_EX + "usage:   " + reset + "python3 ggc.py {-w, -o, -v, -h} SCRIPT.C [SCRIPT2.C, ...]")
    print(tag + Fore.LIGHTYELLOW_EX + "flags:   " + reset + "-w: activate -Wall flag (warnings)")
    print(tag + Fore.LIGHTYELLOW_EX + "\t\t" + reset + "-o: deactivate automatic removal of *.o files.")
    print(tag + Fore.LIGHTYELLOW_EX + "\t\t" + reset + "-v: verify that a executable script exists after finishing.")
    print(tag + Fore.LIGHTYELLOW_EX + "\t\t" + reset + "-e: enable library mode to append more than one .o file into one executable.")
    print(tag + Fore.LIGHTYELLOW_EX + "\t\t" + reset + "-m: enable -lm tag.")
    print(tag + Fore.LIGHTYELLOW_EX + "\t\t" + reset + "-n: disable -O3 optimization.")
    print(tag + Fore.LIGHTYELLOW_EX + "\t\t" + reset + "-h: display this help message.")


def redirect(x, i): # flag detection in parameters
    global alert, cleanup, verify, libraries, math, noOptimization
    if len(x) == 2: # only read flags if they are one character long.

        readFlag = False
        if(x == "-w"): alert = True ; readFlag = True
        elif(x == "-o"): cleanup = False ; readFlag = True
        elif(x == "-v"): verify = True ; readFlag = True
        elif(x == "-e"): libraries = True ; readFlag = True
        elif(x == "-m"): math = True ; readFlag = True
        elif(x == "-h"): readFlag = True
        elif(x == "-n"): noOptimization = True ; readFlag = True

        # print read flag on terminal.
        if readFlag: print(tag + reset + "read '" + x + "' flag.")
        if x == "-h": help()
    else: help() ; exit()

def process(n): # general script tasks
    global alert, verify, cleanup, tag, libraries, math, noOptimization
    x = path.splitext(n)[0] # separates file's name from ext
    if not path.splitext(n)[1] == ".c":
        warning("badext") # only works with files with '.c' ext
    print(tag + Fore.LIGHTBLUE_EX +
        "target file: " + Style.RESET_ALL + x)

    ex = "gcc -c "
    if math: ex += "-lm "
    if alert: ex += "-Wall "
    if not noOptimization: ex += "-O3 "
    ex += x + ".c"
    system(ex)
    if libraries is False:
        system("gcc " + x + ".o -o " + x)
        if cleanup is True: system("rm " + x + ".o")
        print(tag + Fore.GREEN +
             "completed all tasks." + Style.RESET_ALL)

    if verify == True:
        if path.isfile(x):
            print(tag +
                  Fore.YELLOW + "successfully verified.")
        else: warning("failver")

i = 1 # the first parameter isn't read
verify = False # by default, this doesn't verify a valid output
cleanup = True # by default, the *.o file is deleted
alert = False # by default, the -Wall flag is disabled
libraries = False # by default, library mode is disabled
math = False # by default, -lm is disabled
noOptimization = False # by default, -O3 is enabled
tag = Fore.LIGHTMAGENTA_EX + "ggc.py "

print(tag + reset +
     "detected " + str(len(argv) - 1) + " parameter(s).")
if(i == len(argv)): warning("noparm") # there needs to be at least one parameter
while(i < len(argv)): # read all parameters in order
    if(argv[i][0:1:] == '-'): redirect(argv[i], i)
    else: process(argv[i])
    i += 1
if libraries == True:
    a = "gcc " # generates combined string with all parameters to compile into one script
    for b in range(2, len(argv)):
        a += path.splitext(argv[b])[0] + ".o "
    a += "-o " + path.splitext(argv[2])[0]
    system(a)
    print(tag + Fore.GREEN + "completed all tasks.")
