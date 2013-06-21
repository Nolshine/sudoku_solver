"""
Sudoku Solving Algorithm

takes in a 9*9 2D array, partially filled with digits from 1 to 9.

0 means no digit.
1-9 each corresponds to its respective self.
"""

puzzle = [[0,0,0,0,9,0,4,0,0],
          [9,7,0,0,0,1,0,0,0],
          [0,0,0,6,2,8,0,0,1],
          [0,4,6,5,0,0,0,0,0],
          [0,5,9,0,0,0,7,6,0],
          [0,0,0,0,0,4,1,2,0],
          [8,0,0,4,5,6,0,0,0],
          [0,0,0,2,0,0,0,4,8],
          [0,0,7,0,8,0,0,0,0]]


##def check_possibles(row, puzzle):
##    #start with a fresh possible
##    possibles = []
##    for column in range(len(row)):
