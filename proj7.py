'''
Will Fraisl
'''

import re
import random
from collections import OrderedDict

def clean_file():
    #clean file into list of words
    file = open('100-0.txt','r') #open file
    lines = file.read().splitlines() #split file into lines
    lines = lines[140:149259] #remove garbage at beginning and end
    lines = [line for line in lines if line] #remove empty strings
    lines = [re.sub(r'[\xe2\x80\x99]', '\'', line) for line in lines] #replace unicode apostophe
    #TODO remove other unicode symbols
    lines = [re.findall(r'[a-zA-Z\']+', line) for line in lines] #remove non-word characters
    words = [word for line in lines for word in ['<s>'] + line + ['</s>']] #flatten list and add line markers
    words = [word.lower() for word in words] #make all words lowercase
    words = [re.sub(r'\'\'\'','\'',word) for word in words] #remove weird triple quotes
    return words

def main():
    words = clean_file()

    #unigrams
    unigram_words = [re.sub(r'<s>','',word) for word in words]
    unigram_words = [re.sub(r'</s>','',word) for word in unigram_words]
    unigram_words = [word for word in unigram_words if word] #remove empty strings

    unigram_dictionary_of_tokens = OrderedDict()
    for token in unigram_words:
        if token in unigram_dictionary_of_tokens:
            unigram_dictionary_of_tokens[token] += 1
        else:
            unigram_dictionary_of_tokens[token] = 1

    unigram_total = len(unigram_words)

    unigram_relative_freq = {key:float(item)/total for key, item in unigram_dictionary_of_tokens.items()}
    
    prev = 0
    unigram_cumulative_prob = OrderedDict()
    for key, val in unigram_relative_freq.items():
        unigram_cumulative_prob[key] = prev + val
        prev = unigram_cumulative_prob[key]

    #bigrams
     

    #create 5 sentences of 12 words long
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

main()