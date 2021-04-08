"""
Usage:
    Peeping-Tom-Converter.py (-i FILE -o FILE)

Options:
    -h, --help             Prints this Message
    -i FILE, --input=FILE  PeepingTom.txt
    -o FILE, --output=FILE Your output file location
"""

#Created by: [Telekors] - https://github.com/Telekors

from docopt import docopt
import sys, socket

def main(input_file, output_file):
    new_urls = []
    f = open(input_file,"r")
    for url in f:
        try:
            stripped = url.strip('\n').replace('//','').split(":")
            domain_name = socket.gethostbyaddr(stripped[1])
            tmpstring = (stripped[0] + "://" + domain_name[0] + ":" + stripped[2])
            new_urls.append(tmpstring)
        except:
            continue
    f = open(output_file, "w")
    #f.write("IP Address, Port\n")
    for out_url in new_urls:
        print(out_url)
        f.write(out_url + "\n")
    f.close()

if __name__ == "__main__":
    arguments = docopt(__doc__, version='Gnmap Parser Checker 1.0')
    main(arguments["--input"], arguments["--output"])
