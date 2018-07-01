#!/usr/bin/python3

import os


print('Current dir contents:',os.listdir())

infile=open('inputfile.txt')
total=0

line=infile.readline()
while line:
    number=int(line)
    total+=number
    #print(number)
    line=infile.readline()

print(total)
totalstring=str(total)
print('first 10 digits: ') 
nrdigits=10
print(totalstring[0:nrdigits])

