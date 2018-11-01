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

    #unigram words (remove <s> and </s>)
    unigram_words = [re.sub(r'<s>','',word) for word in words]
    unigram_words = [re.sub(r'</s>','',word) for word in unigram_words]
    unigram_words = [word for word in unigram_words if word] #remove empty strings

    unigram_dictionary_of_tokens = OrderedDict()
    for token in unigram_words[:-1]:
        if token in unigram_dictionary_of_tokens:
            unigram_dictionary_of_tokens[token] += 1
        else:
            unigram_dictionary_of_tokens[token] = 1

    bigram_dictionary_of_tokens = OrderedDict()
    for i in range(len(words)-1):
        if words[i] +' '+ words[i+1] in bigram_dictionary_of_tokens:
            bigram_dictionary_of_tokens[words[i] +' '+ words[i+1]] += 1
        else:
            bigram_dictionary_of_tokens[words[i] +' '+ words[i+1]] = 1

    trigram_dictionary_of_tokens = OrderedDict()
    for i in range(len(words)-2):
        if words[i] +' '+ words[i+1] +' '+ words[i+2] in trigram_dictionary_of_tokens:
            trigram_dictionary_of_tokens[words[i] +' '+ words[i+1] +' '+ words[i+2]] += 1
        else:
            trigram_dictionary_of_tokens[words[i] +' '+ words[i+1] +' '+ words[i+2]] = 1

    quadgram_dictionary_of_tokens = OrderedDict()
    for i in range(len(words)-3):
        if words[i] +' '+ words[i+1] +' '+ words[i+2] +' '+ words[i+3] in quadgram_dictionary_of_tokens:
            quadgram_dictionary_of_tokens[words[i] +' '+ words[i+1] +' '+ words[i+2] +' '+ words[i+3]] += 1
        else:
            quadgram_dictionary_of_tokens[words[i] +' '+ words[i+1] +' '+ words[i+2] +' '+ words[i+3]] = 1

    unigram_total = len(unigram_words)
    bigram_total = len(words)-1
    trigram_total = len(words)-2
    quadgram_total = len(words)-3

    del bigram_dictionary_of_tokens['</s> <s>']
    del trigram_dictionary_of_tokens['</s> <s>']
    del quadgram_dictionary_of_tokens['</s> <s>']

    unigram_relative_freq = {key:float(item)/unigram_total for key, item in unigram_dictionary_of_tokens.items()}
    bigram_relative_freq = {key:float(item)/bigram_total for key, item in bigram_dictionary_of_tokens.items()}
    trigram_relative_freq = {key:float(item)/trigram_total for key, item in trigram_dictionary_of_tokens.items()}
    quadgram_relative_freq = {key:float(item)/quadgram_total for key, item in quadgram_dictionary_of_tokens.items()}

    prev = 0
    unigram_cumulative_prob = OrderedDict()
    for key, val in unigram_relative_freq.items():
        unigram_cumulative_prob[key] = prev + val
        prev = unigram_cumulative_prob[key]

    prev = 0
    bigram_cumulative_prob = OrderedDict()
    for key, val in bigram_relative_freq.items():
        bigram_cumulative_prob[key] = prev + val
        prev = bigram_cumulative_prob[key]

    prev = 0
    trigram_cumulative_prob = OrderedDict()
    for key, val in trigram_relative_freq.items():
        trigram_cumulative_prob[key] = prev + val
        prev = trigram_cumulative_prob[key]

    prev = 0
    quadgram_cumulative_prob = OrderedDict()
    for key, val in quadgram_relative_freq.items():
        quadgram_cumulative_prob[key] = prev + val
        prev = quadgram_cumulative_prob[key]
     
    #unigram
    print 'Unigram Sentences:'
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

    #bigram
    print '\nBigram Sentences:'
    for _ in range(5):
        sentence = ''
        for i in range(6):
            rand = random.random()
            for key, val in bigram_cumulative_prob.items():
                if val > rand:
                    word = key
                    break
            sentence += word + ' '
        sentence = sentence[:-1] 
        sentence += '.'
        sentence = sentence.capitalize()
        print(sentence)

    #trigram
    print '\nTrigram Sentences:'
    for _ in range(5):
        sentence = ''
        for i in range(4):
            rand = random.random()
            for key, val in trigram_cumulative_prob.items():
                if val > rand:
                    word = key
                    break
            sentence += word + ' '
        sentence = sentence[:-1] 
        sentence += '.'
        sentence = sentence.capitalize()
        print(sentence)

    #quadgram
    print '\nQuadgram Sentences:'
    for _ in range(5):
        sentence = ''
        for i in range(3):
            rand = random.random()
            for key, val in quadgram_cumulative_prob.items():
                if val > rand:
                    word = key
                    break
            sentence += word + ' '
        sentence = sentence[:-1] 
        sentence += '.'
        sentence = sentence.capitalize()
        print(sentence)

main()