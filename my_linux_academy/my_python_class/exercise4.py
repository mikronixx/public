#!/usr/bin/env python
message = raw_input("What is your message ")
count = (raw_input("enter a number "))
if count:
 count = int(count)
else:
 count = 1
#add a function
def noise(x,y):
   for i in range (0,x):
    print ("%s" %y)

noise(count,message)
