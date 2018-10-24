'''
Class: CPSC 475
Team Member 1: Will Fraisl
Team Member 2: N/A
GU Username of project lead: wfraisl
Pgm Name: proj6.py
Desrciption: Creates 5 sentences of 10 words long using unigrams
    from brown corpus.
Usage: python proj5.py
Due: 10/26/18
'''

from nltk.corpus import brown
import re
import random
from collections import OrderedDict 

def main():
    brown_words = brown.words(categories='editorial')
    tokens = [item.encode('ascii') for item in brown_words]

    #remove punctuation and lowercase
    tokens = [re.sub(r'[.]', '', item).lower() for item in tokens]
    
    dictionary_of_tokens = OrderedDict()
    for token in tokens:
        if token in dictionary_of_tokens:
            dictionary_of_tokens[token] += 1
        else:
            dictionary_of_tokens[token] = 1

    total = len(tokens)

    relative_freq = {key:float(item)/total for key, item in dictionary_of_tokens.items()}
    
    prev = 0
    cumulative_prob = OrderedDict()
    for key, val in relative_freq.items():
        cumulative_prob[key] = prev + val
        prev = cumulative_prob[key]
    
    #create 5 sentences of 10 words long
    for _ in range(5):
        sentence = ''
        for _ in range(10):
            rand = random.random()
            for key, val in cumulative_prob.items():
                if val > rand:
                    word = key
                    break
            sentence += word + ' '
        sentence = sentence[:-1] 
        sentence += '.'
        sentence = sentence.capitalize()
        print(sentence)
        
main()