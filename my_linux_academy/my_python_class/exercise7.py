#!/usr/bin/env python
import argparse

parser = argparse.ArgumentParser (description='Prints the specified line_number from file_name to the screen. The user will specify this as you would expect, not using zero as the first line')
parser.add_argument('filename', help='enter a filename to read')
parser.add_argument('line_number', type=int,  help='enter a line number')
parser.add_argument('--version', '-v',  action='version', version='1.0')
args = parser.parse_args()
#print(args.filename)
#print(args.line_number)
try: 
 f = open(args.filename)
except IOError as err:
 print("file not found")
else:
 f = open(args.filename)
 line_number = int(args.line_number)
 if line_number == 0:
   print "fool do not use 0"
   exit
 else:
   line_number = int(args.line_number) - 1
   mycontent = f.readlines() #this can be combined with open
   try:
    print mycontent[line_number]
   except IndexError as interr:
    print(" file has less than %s lines" % (line_number + 1))
