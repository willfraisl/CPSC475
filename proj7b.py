'''
Class: CPSC 475
Team Member 1: Will Fraisl
Team Member 2: N/A
GU Username of project lead: wfraisl
Pgm Name: proj7b.py
Desrciption: Prints shakespeare sentences using grams
Usage: python proj7b.py
Due: 11/9/18
'''

import random
import pickle

def make_sentence(cumulative_prob, size_of_gram, num_grams, show_markers):
    sentence = ''
    for i in range(num_grams):
        rand = random.random()
        gram = get_gram(cumulative_prob, rand)
        if i==0 or i==num_grams-1:
            while((i==0 and gram[0]!='<s>') or (i==num_grams-1 and gram[size_of_gram-1]!='</s>')):
                rand = random.random()
                gram = get_gram(cumulative_prob, rand)
        else:
            while(set(('<s>',)).issubset(gram) or set(('</s>',)).issubset(gram)):
                rand = random.random()
                gram = get_gram(cumulative_prob, rand)
        for word in gram:
            sentence += word + ' '
    sentence = sentence[:-1] 
    sentence = sentence[:4] + sentence[4].upper() + sentence[5:-5] + '.' + sentence[-5:]
    if not show_markers:
        sentence = sentence[4:-4]
    return sentence

def get_gram(cumulative_prob, rand):
    for tup in cumulative_prob:
        if tup[1] > rand:
            return tup[0]

def main():
    #reading in pickle file
    fin = open('proj7b.pkl', 'rb')
    cumulative_probs = pickle.load(fin)
    fin.close()
    show_markers = input('Would you like to see line markers? (True/False): ')

    #print unigram sentences
    print '\nUnigram Sentences:'
    for _ in range(5):
        sentence = ''
        for _ in range(12):
            rand = random.random()
            for tup in cumulative_probs[0]:
                if tup[1] > rand:
                    word = tup[0]
                    break
            sentence += word + ' '
        sentence = sentence[:-1] 
        sentence += '.'
        sentence = sentence.capitalize()
        print(sentence)

    #print bigram sentences
    print '\nBigram Sentences:'
    for _ in range(5):
        print make_sentence(cumulative_probs[1], 2, 6, show_markers)

    #print trigram sentences
    print '\nTrigram Sentences:'
    for _ in range(5):
        print make_sentence(cumulative_probs[2], 3, 4, show_markers)

    #print quadgram sentences
    print '\nQuadgram Sentences:'
    for _ in range(5):
        print make_sentence(cumulative_probs[3], 4, 3, show_markers)


main()