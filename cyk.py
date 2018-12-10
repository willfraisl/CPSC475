'''
Class: CPSC 475
Team Member 1: Will Fraisl
Team Member 2: N/A
GU Username of project lead: wfraisl
Pgm Name: cyk.py
Desrciption: demonstrates the cyk parser
Usage: python cyk.py cfg1.txt strng1.txt
Due: 12/13/18
'''

import sys
import numpy


def main():
    # checking usage
    if len(sys.argv) != 3:
        print "usage: python cyk.py cfg.txt strng.txt"
        exit(1)

    # read grammar in to have language
    lang = read_lang(sys.argv[1])

    # getting string
    str = open(sys.argv[2], 'r').read().split()
    if len(str) == 1:
        str = list(str[0])

    # print if string is in language based on cyk
    print is_cyk(lang, str)


def read_lang(file_name):
    f = open(file_name, 'r')
    lang = {}
    for line in f:
        line = line.split()
        key = line[0]
        if not key in lang:
            lang[key] = []
        for val in line[2:]:
            lang[key].append(val)
    f.close()
    return lang


def is_cyk(lang, str):
    str_len = len(str)
    # setting up matrix
    mat = [[[] for i in range(str_len+1)] for j in range(str_len+1)]

    # setting diagonal of matrix with terminal rules
    for i in range(1, str_len+1):
        for key, vals in lang.items():
            if str[i-1] in vals:
                mat[i][i].append(key)

    # filling the rest of the matrix
    for step in range(2, str_len+1):
        for i in range(1, str_len - step + 2):
            for k in range(i, i + step - 1):
                for b in mat[i][k]:
                    for c in mat[k+1][i+step-1]:
                        for key, vals in lang.items():
                            if b+'+'+c in vals:
                                mat[i][i+step-1].append(key)

    # return true if "S" in in top right
    return "S" in mat[1][str_len]


main()
