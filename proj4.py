'''
Class: CPSC 475
Team Member 1: Will Fraisl
Team Member 2: N/A
GU Username of project lead: wfraisl
Pgm Name: proj4.py
Desrciption: Takes in a name from command line and returns soundex encoding
Usage: python proj4.py <name>
Due: 9/26/18
'''

import re
import sys

def main():
    if len(sys.argv) != 2:
        print('Program uses format: python proj4.py <name>')
        return
    name = sys.argv[1]
    first_letter = name[0]
    name = name[1:].lower()
    step_a = a(name)
    step_b = b(step_a)
    step_c = c(step_b)
    step_d = d(step_c)
    print(first_letter + step_d)

def a(str):
    return re.sub(r'[aehiouwy]','*',str)

def b(str):
    str = re.sub(r'[bfpv]','1',str)
    str = re.sub(r'[cgjkqsxz]','2',str)
    str = re.sub(r'[dt]','3',str)
    str = re.sub(r'[l]','4',str)
    str = re.sub(r'[mn]','5',str)
    str = re.sub(r'[r]','6',str)
    return str

def c(str):
    str = re.sub(r'(\d)\1+',r'\1',str)
    str = re.sub(r'[*]','',str)
    return str

def d(str):
    str = str + '000'
    return str[:3]

main()