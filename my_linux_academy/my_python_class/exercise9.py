#!/usr/bin/env python
import argparse
import subprocess
import os
import sys

parser = argparse.ArgumentParser (description='seeks open ports to kill')
parser.add_argument('port', help='enter a port ypu want killed')
args = parser.parse_args()
mystring = "-i4TCP:"
#print mystring
myport = str(args.port)
#print myport
myarg = mystring + myport
#print myarg
try: 
 pid = subprocess.Popen(('lsof', '-n',myarg ), stdout=subprocess.PIPE)
 output = subprocess.check_output(('grep', 'LISTEN'), stdin=pid.stdout).split()
except subprocess.CalledProcessError as err :
 print "  Nothing listening on %s " %(myport)
 sys.exit(2)
else:
 pid = subprocess.Popen(('lsof', '-n',myarg ), stdout=subprocess.PIPE)
 output = subprocess.check_output(('grep', 'LISTEN'), stdin=pid.stdout).split()
 #print output
 print "  killing process on port %s " %(myport)
 killpid = int(output[1])
 os.kill(killpid,9)
 sys.exit(0)


