#!/usr/bin/env python
import argparse
import requests
import sys

parser = argparse.ArgumentParser (description='writes a url to file')
parser.add_argument('myurl',   help='enter a url')
parser.add_argument('myfile', help='outputfile')
parser.add_argument('--content', '-c' , default='html', choices=['html', 'json'] , help='content output format.  default html')
args = parser.parse_args()

r = requests.get(args.myurl ,verify=False )

if args.content == 'json':
    try:
        mycontent = r.json()
    except ValueError:
        print("Error not  JSON")
        sys.exit(1)
else: 
    mycontent = r.text

file = open(args.myfile, 'w+')
file.write(mycontent.encode("UTF-8"))






