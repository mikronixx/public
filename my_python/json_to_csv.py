#!/usr/bin/env python
"""tool to convert json to csv. tested on centos6.10"""
#https://medium.com/@gabrielpires/how-to-convert-a-json-file-to-csv-python-script-a9ff0a3f906e
import csv
import json
import sys
reload(sys)
sys.setdefaultencoding("UTF-8")

myinfile = sys.argv[1]
myoutfile = sys.argv[2]
#print myinfile #debug
json_data = open(myinfile)
data = json.load(json_data)
#print data #debug

output  = csv.writer(open(myoutfile,"wb+"))
output.writerow(data[0].keys())  # header row
for row in data:
        output.writerow(row.values()) #values row
