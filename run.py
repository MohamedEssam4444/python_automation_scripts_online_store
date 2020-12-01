#!/usr/bin/env python3
import os
import sys
import json
import re
import requests
dct=dict()
s=list()
# dct={'name':'','weight':'' ,'description':'','image_name':''}
filepath='supplier-data/descriptions/'
files_in_current_directory=os.listdir(filepath)
line1=list()
for file in files_in_current_directory:
    i=os.path.basename(file)
    print(i)
    f, e = os.path.splitext(file)
    with open(filepath+i,'r') as f:
        for line in f:
            line = line.rstrip()
            # print(line)
            line3=line.split('\n')
            line1.append(line3)
        #to remove sqaure brackets nested in list
        line1=str(line1).replace('[','').replace(']','')
        line1=list(eval(line1))
        pattern=r"([0-9+]*)" #pattern to get only integer and skip any non integer value
        result1=re.search(pattern,line1[1])
        print(result1[1])
        result2=re.search(pattern,i)

        print(result2[1])
        dct.update({'name':line1[0],'weight':int(result1[1]),'description':line1[2],'image_name':str(result2[1])+".jpeg"})
        print(dct)
        response = requests.post("http://35.225.243.253/fruits", json=dct) #webserver ip
        if response.status_code != 200:
            print('Error posting the feedback')
        line1.clear()
