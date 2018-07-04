#!/usr/bin/env python
filename = raw_input("enter a filename  ")
while True:
 stuff= raw_input("enter stuff  ")
 if stuff == "":
  print "done"
  break
 else: 
  myfile =  open(filename ,"a") 
  myfile.write(stuff + "\n")

