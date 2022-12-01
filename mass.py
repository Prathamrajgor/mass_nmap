import os
import threading
import getopt
import sys

def scan(host,flags,output):
    os.system(f"nmap {flags} {host} | tee -a {output} ")
def main():
    argv = sys.argv[1:]
    opts, args = getopt.getopt(argv, "i:f:o:")
    file=None
    flags=None
    output=None
    try:    
        for opt, arg in opts:
            if opt in ['-i']:
                file = arg.strip()
            elif opt in ['-f']:
                flags = arg.strip()
            elif opt in ['-o']:
                output=arg.strip()
    except:
        print("[*] Wrong or improprt input\n")
    os.system(f"echo > {output}")
    try:
        print(f"[+] Reading domains from the file.")
        f=open(f"{file}").read().splitlines()
        print(f"[+] File read successfully\n")
    except:
        print(f"[*] Error opening the file {file}. Check your input again\n")
    threads=[None]*len(f)
    print(f"[+] Starting mass nmap scan.\n")
    for i in range(len(f)):
        threads[i]=threading.Thread(target=scan,args=(f[i].strip(),flags,output,))
        threads[i].start()
    for i in range(len(f)):
        threads[i].join()
    print(f"[+] Scan completed succesfully.\n Results outputted to {output}.")    

if __name__=="__main__":
    main()