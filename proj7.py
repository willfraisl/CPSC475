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

import re
import random
from collections import OrderedDict

def clean_file():
    #clean file into list of words
    file = open('100-0.txt','r') #open file
    lines = file.read().splitlines() #split file into lines
    lines = lines[140:149259] #remove garbage at beginning and end
    lines = [re.sub(r'\xe2\x80\x99', '\'', line) for line in lines] #replace unicode apostophe
    lines = [re.findall(r'[a-zA-Z\']+', line) for line in lines] #remove non-word characters
    lines = [[word.lower() for word in line] for line in lines if line] #make all words lowercase and remove empty
    return lines

def create_dictionary(num, lines):
    dict = OrderedDict()
    total = 0
    for line in lines:
        line = ['<s>'] + line + ['</s>']
        for i in range(len(line)-num+1):
            key = tuple(line[i+j] for j in range(num))
            total += 1
            if key in dict:
                dict[key] += 1
            else:
                dict[key] = 1
    return dict, total

def create_cumulative_prob(relative_freq):
    prev = 0
    cumulative_prob = OrderedDict()
    for key, val in relative_freq.items():
        cumulative_prob[key] = prev + val
        prev = cumulative_prob[key]
    return cumulative_prob

def make_sentence(cumulative_prob, size_of_gram, num_grams):
    sentence = ''
    for i in range(num_grams):
        rand = random.random()
        gram = get_gram(cumulative_prob, rand)
        while((i==0 and gram[0]!='<s>') or (i==num_grams-1 and gram[size_of_gram-1]!='</s>')):
            rand = random.random()
            gram = get_gram(cumulative_prob, rand)
        for word in gram:
            sentence += word + ' '
    sentence = sentence[:-1] 
    sentence = sentence.capitalize()
    return sentence

def get_gram(cumulative_prob, rand):
    for key, val in cumulative_prob.items():
        if val > rand:
            return key

def main():
    show_markers = input('Would you like to see line markers? (True/False): ')

    #cleaning file
    lines = clean_file()

    #creating unigram dictionary
    unigram_dictionary = OrderedDict()
    unigram_total = 0
    for line in lines:
        for word in line:
            unigram_total += 1
            if word in unigram_dictionary:
                unigram_dictionary[word] += 1
            else:
                unigram_dictionary[word] = 1

    #creating > 1 dictionarys
    bigram_dictionary, bigram_total = create_dictionary(2,lines)
    trigram_dictionary, trigram_total = create_dictionary(3,lines)
    quadgram_dictionary, quadgram_total = create_dictionary(4,lines)

    #creating relative frequencies
    unigram_relative_freq = {key:float(item)/unigram_total for key, item in unigram_dictionary.items()}
    bigram_relative_freq = {key:float(item)/bigram_total for key, item in bigram_dictionary.items()}
    trigram_relative_freq = {key:float(item)/trigram_total for key, item in trigram_dictionary.items()}
    quadgram_relative_freq = {key:float(item)/quadgram_total for key, item in quadgram_dictionary.items()}

    unigram_cumulative_prob = create_cumulative_prob(unigram_relative_freq)
    bigram_cumulative_prob = create_cumulative_prob(bigram_relative_freq)
    trigram_cumulative_prob = create_cumulative_prob(trigram_relative_freq)
    quadgram_cumulative_prob = create_cumulative_prob(quadgram_relative_freq)

    #print unigram sentences
    print '\nUnigram Sentences:'
    for _ in range(5):
        sentence = ''
        for _ in range(12):
            rand = random.random()
            for key, val in unigram_cumulative_prob.items():
                if val > rand:
                    word = key
                    break
            sentence += word + ' '
        sentence = sentence[:-1] 
        sentence += '.'
        sentence = sentence.capitalize()
        print(sentence)

    #print bigram sentences
    print '\nBigram Sentences:'
    for _ in range(5):
        print make_sentence(bigram_cumulative_prob, 2, 6)

    #print trigram sentences
    print '\nTrigram Sentences:'
    for _ in range(5):
        print make_sentence(trigram_cumulative_prob, 3, 4)

    #print quadgram sentences
    print '\nQuadgram Sentences:'
    for _ in range(5):
        print make_sentence(quadgram_cumulative_prob, 4, 3)


main()