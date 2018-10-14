'''
Class: CPSC 475
Team Member 1: Will Fraisl
Team Member 2: N/A
GU Username of project lead: wfraisl
Pgm Name: proj3.py
Desrciption: Asks user for a word to count in inaugural speeches and graphs
result
Due: 9/18/18
'''

import pickle
import matplotlib.pyplot as plt

def main():
    #reading in pickle file
    fin = open('proj3.pkl', 'rb')
    list_of_addresses = pickle.load(fin)
    fin.close()
    key_word = raw_input("What word are you interested in: ")

    #counting words in each inaugural address
    years = [1789]
    list_of_counts = []
    for address in list_of_addresses:
        counter = 0
        for word in address:
            if word == key_word:
                counter += 1
        list_of_counts.append(counter)
        years.append(years[-1] +4)

    #displaying results
    years.pop()
    plt.plot(years, list_of_counts)
    plt.xlabel("Years")
    plt.ylabel("Occurrences of " + key_word)
    plt.show()

main()