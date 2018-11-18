'''
Class: CPSC 475
Team Member 1: Will Fraisl
Team Member 2: N/A
GU Username of project lead: wfraisl
Pgm Name: test2a.py
Desrciption: demonstrates the forward algorithm
Usage: python test2a.py matA.txt matB.txt <sequence>
Due: 11/16/18
'''

import csv
import numpy
import sys


def main():
    #check for correct usage
    if len(sys.argv) != 4:
        print "usage: python test2a.py matA.txt matB.txt <sequence>"
        exit(1)

    #reading in A matrix as numpy array
    matA = csv.reader(open(sys.argv[1], 'rb'), delimiter= ',')
    matA = list(matA)
    matA = numpy.array(matA).astype('float')

    #reading in B matrix as numpy array
    matB = csv.reader(open(sys.argv[2], 'rb'), delimiter= ',')
    matB = list(matB)
    matB = numpy.array(matB).astype('float')

    #reading in sequence
    seq = [int(digit) for digit in sys.argv[3]]

    #call forward algorithm
    seq_prob = forward(matA, matB, seq)
    
    print "sequnce probability:", seq_prob

def forward(matA, matB, seq):
    #creates array forward algorithm will fill
    matC = numpy.zeros(shape=(matA.shape[0]-2,len(seq)))

    #calculate first column of probabilities
    for i in range(matC.shape[0]):
        matC[i][0] = matA[0][i+1] * matB[i+1][seq[0]-1]

    #calculate the rest of columns of probabilities
    for col in range(1, matC.shape[1]):
        for row in range(matC.shape[0]):
            for i in range(matC.shape[0]):
                matC[row][col] += matC[i][col-1] * matA[i+1][row+1] * matB[row+1][seq[col]-1]

    #calculate end probabillity from last column
    seq_prob = 0
    for i in range(matC.shape[0]):
        seq_prob += matC[i][-1] * matA[i+1][3]

    return seq_prob
    
main()