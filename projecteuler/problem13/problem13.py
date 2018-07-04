#!/usr/bin/python3

infile=open('inputfile.txt')
total=0

for line in infile:
    number=int(line)
    total+=number

print(total)
totalstring=str(total)

print('first 10 digits: ')
nrdigits=10
print(totalstring[0:nrdigits])

