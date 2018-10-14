'''
Class: CPSC 475
Team Member 1: Will Fraisl
Team Member 2: N/A
GU Username of project lead: wfraisl
Pgm Name: proj5.py
Desrciption: Takes 2 words and finds min edit distance and alignment
Usage: python proj4.py <source> <target>
Due: 10/5/18
'''

import sys

def main():
    if len(sys.argv) != 3:
        print('Usage: python proj5.py <source> <target>')
        exit
    else:
        med, matrix = min_edit_distance(sys.argv[1], sys.argv[2])
        print 'Minimum edit distance: {0}'.format(med)
        print_alignment(matrix, sys.argv[1], sys.argv[2])

class element():
    def __init__(self, num, action):
        self.num = num
        self.action = action

def min_edit_distance(source, target):
    n = len(target)
    m = len(source)
    matrix = [[element(0,'none') for j in range(m+1)] for i in range(n+1)]
    matrix[0][0] = element(0,'none')
    for i in range(1,n+1):
        matrix[i][0] = element(matrix[i-1][0].num + 1, 'insert')
    for j in range(1,m+1):
        matrix[0][j] = element(matrix[0][j-1].num + 1, 'delete')
    for i in range(1,n+1):
        for j in range(1,m+1):
            if source[j-1] == target[i-1]:
                sub_cost = 0
            else:
                sub_cost = 2
            num_to_enter = min(matrix[i-1][j].num+1, matrix[i][j-1].num+1, matrix[i-1][j-1].num+sub_cost)
            if matrix[i-1][j-1].num+sub_cost == num_to_enter:
                matrix[i][j] = element(num_to_enter, 'sub')
            elif matrix[i-1][j].num+1 == num_to_enter:
                matrix[i][j] = element(num_to_enter, 'insert')
            else:
                matrix[i][j] = element(num_to_enter, 'delete')
    return matrix[n][m].num, matrix

def print_alignment(matrix, source, target):
    i = len(target)
    j = len(source)
    source_align = ''
    target_align = ''
    type_align = ''
    while i > 0 or j > 0:
        if matrix[i][j].action == 'sub':
            source_align = source[j-1] + source_align
            target_align = target[i-1] + target_align
            if source[j-1] == target[i-1]:
                type_align = ' ' + type_align
            else:
                type_align = 's' + type_align
            i -= 1
            j -= 1
        elif matrix[i][j].action == 'insert':
            source_align = '*' + source_align
            target_align = target[i-1] + target_align
            type_align = 'i' + type_align
            i -= 1
        else:
            source_align = source[j-1] + source_align
            target_align = '*' + target_align
            type_align = 'd' + type_align
            j -= 1
    print source_align
    print target_align
    print type_align

main()