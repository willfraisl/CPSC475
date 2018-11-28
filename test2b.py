'''
Class: CPSC 475
Team Member 1: Will Fraisl
Team Member 2: N/A
GU Username of project lead: wfraisl
Pgm Name: test2b.py
Desrciption: demonstrates the viterbi algorithm
Usage: python test2b.py matA.csv matB.csv <sequence>
Due: 11/30/18
'''

import csv
import numpy
import sys


def main():
    # check for correct usage
    if len(sys.argv) != 4:
        print "usage: python test2a.py matA.csv matB.csv <sequence>"
        exit(1)

    # reading in A matrix as numpy array
    matA = csv.reader(open(sys.argv[1], 'rb'), delimiter=',')
    matA = list(matA)
    matA = numpy.array(matA).astype('float')

    # reading in B matrix as numpy array
    matB = csv.reader(open(sys.argv[2], 'rb'), delimiter=',')
    matB = list(matB)
    matB = numpy.array(matB).astype('float')

    #reading in sequence
    seq = [int(digit) for digit in sys.argv[3]]

    # call viterbi algorithm
    weather = viterbi(matA, matB, seq)

    print weather


def viterbi(matA, matB, seq):
    # creates array forward algorithm will fill
    matC = numpy.zeros(shape=(matA.shape[0]-2, len(seq)))
    backpointers = numpy.zeros(shape=matC.shape).astype('int')

    # calculate first column of probabilities
    for i in range(matC.shape[0]):
        matC[i][0] = matA[0][i+1] * matB[i+1][seq[0]-1]
        backpointers[i][0] = i

    # calculate the rest of columns of probabilities
    for col in range(1, matC.shape[1]):
        for row in range(matC.shape[0]):
            curr_max = 0
            curr_max_row = -1
            for i in range(matC.shape[0]):
                curr = matC[i][col-1] * \
                    matA[i+1][row+1] * matB[row+1][seq[col]-1]
                if curr > curr_max:
                    curr_max = curr
                    curr_max_row = i
            matC[row][col] = curr_max
            backpointers[row][col] = curr_max_row

    # follow backpointers to find weather sequence
    weather = []
    # get index of largest element of last column
    end_index = numpy.argmax(matC, axis=0)[-1]

    weather.append(end_index)
    curr = backpointers[end_index][-1]
    # go backwards through backpointers matrix
    for i in range(backpointers.shape[1]-2, -1, -1):
        weather.append(curr)
        curr = backpointers[curr][i]

    # change to H and C
    weather.reverse()
    weather_seq = ''
    for elem in weather:
        if elem == 0:
            weather_seq += 'C'
        else:
            weather_seq += 'H'
        weather_seq += ' '

    return weather_seq


main()
