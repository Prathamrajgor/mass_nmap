# mass_nmap
A simple Python script to perform mass nmap scans. 
## Usage
### How to run?
    Enter the command:
    python mass.py 
### Flags:
    -i: This -i flag takes the name of the input file which contains the hosts.
    -f: The -f flag takes the flags of the nmap scan.
    -o: Takes the name of the file to which you want to output your results.
## Example
    python mass.py -i subdomains.txt -f "-sV -sC" -o output.txt
