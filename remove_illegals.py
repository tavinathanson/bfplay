#!/usr/bin/env python3

import sys, getopt

LEGAL = "+-<>[],."

def remove_illegals(input_file, output_file):
    output_chars = []
    with open(input_file,'r') as f:
        input_file_string = f.read()
        for char in input_file_string:
            if char in LEGAL:
                output_chars.append(char)
    output_file_string = "".join(output_chars)
    f = open(output_file, 'w')
    print(output_file_string, file=f)    

def main(argv):
    input_file = ''
    output_file = ''
    try:
        opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
    except getopt.GetoptError:
        print("test.py -i <input_file> -o <output_file>")
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print("test.py -i <input_file> -o <output_file>")
            sys.exit()
        elif opt in ("-i", "--ifile"):
            input_file = arg
        elif opt in ("-o", "--ofile"):
            output_file = arg
    remove_illegals(input_file, output_file)

if __name__ == "__main__":
   main(sys.argv[1:])

