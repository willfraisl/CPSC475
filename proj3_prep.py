'''
Class: CPSC 475
Team Member 1: Will Fraisl
Team Member 2: N/A
GU Username of project lead: wfraisl
Pgm Name: proj3_prep.py
'''

import nltk
import re
import pickle
from nltk.corpus import inaugural

def main():
    list_of_addresses = []
    for fileid in inaugural.fileids():
        
        list_of_words = inaugural.words(fileid)
        string_of_words = ' '.join(list_of_words)
        alphabetic_words = re.findall(r"\w+", string_of_words)
        list_of_addresses.append(alphabetic_words)
    #print(list_of_addresses)
    fout = open ('proj3.pkl','wb')
    pickle.dump(list_of_addresses,fout)
    fout.close()

main()