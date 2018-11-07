'''
Class: CPSC 475
Team Member 1: Will Fraisl
Team Member 2: N/A
GU Username of project lead: wfraisl
Pgm Name: proj7a.py
Desrciption: Pickles the cumulative probabilities
Usage: python proj7a.py
Due: 11/9/18
'''

import re
import pickle

def clean_file():
    #clean file into list of words
    file = open('shakespeare.txt','r') #open file
    lines = file.read().splitlines() #split file into lines
    lines = [re.sub(r'\xe2\x80\x99', '\'', line) for line in lines] #replace unicode apostophe
    lines = [re.findall(r'[a-zA-Z\']+', line) for line in lines] #remove non-word characters
    lines = [[word.lower() for word in line] for line in lines if len(line) > 4] #make all words lowercase and remove empty
    return lines

def create_dictionary(num, lines):
    dict = {}
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
    cumulative_prob = []
    for tup in relative_freq:
        cumulative_prob.append((tup[0], tup[1] + prev))
        prev += tup[1]
    return cumulative_prob

def main():

    #cleaning file
    lines = clean_file()

    #creating unigram dictionary
    unigram_dictionary = {}
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
    unigram_relative_freq = [(key, float(item)/unigram_total) for key, item in unigram_dictionary.items()]
    bigram_relative_freq = [(key, float(item)/bigram_total) for key, item in bigram_dictionary.items()]
    trigram_relative_freq = [(key, float(item)/trigram_total) for key, item in trigram_dictionary.items()]
    quadgram_relative_freq = [(key, float(item)/quadgram_total) for key, item in quadgram_dictionary.items()]

    cumulative_probs = []
    cumulative_probs.append(create_cumulative_prob(unigram_relative_freq))
    cumulative_probs.append(create_cumulative_prob(bigram_relative_freq))
    cumulative_probs.append(create_cumulative_prob(trigram_relative_freq))
    cumulative_probs.append(create_cumulative_prob(quadgram_relative_freq))

    fout = open ('proj7b.pkl','wb')
    pickle.dump(cumulative_probs,fout)
    fout.close()

main()