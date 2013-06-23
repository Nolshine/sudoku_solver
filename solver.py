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
#must remember that counting starts at 0;
#row 1 is actually row 0.


def row_possibles(puzzle, row):
    #start with a fresh possible range
    possibles = [1,2,3,4,5,6,7,8,9]
    structure = puzzle[row]
    
    for cell in structure:
        #check all cells in the row and remove existing digits from possibles
        if cell != 0:
            if cell in possibles:
                possibles.remove(cell)
    return possibles

def col_possibles(puzzle, column):
    possibles = [1,2,3,4,5,6,7,8,9]
    structure = []
    for row in range(9):
        structure.append(puzzle[row][column])
    for cell in structure:
        if cell != 0:
            if cell in possibles:
                possibles.remove(cell)
    return possibles

def box_possibles(puzzle, row, column):
    possibles = [1,2,3,4,5,6,7,8,9]
    box_row = row * 3
    box_column = column * 3
    structure = []
    for row in range(box_row, (box_row+3)):
        for column in range(box_column, (box_column+3)):
            structure.append(puzzle[row][column])
    for cell in structure:
        if cell != 0:
            if cell in possibles:
                possibles.remove(cell)
    return possibles



print str(row_possibles(puzzle, 0))
#this should print out [1,2,3,5,6,7,8] - check
print str(col_possibles(puzzle, 0))
#this should print out [1,2,3,4,5,6,7] - check
print str(box_possibles(puzzle, 0, 0))
#this should print out [1,2,3,4,5,6,8] - check

#working good, let's test some more
print str(row_possibles(puzzle, 3))
#[1,2,3,7,8,9] - predicted result - check
print str(col_possibles(puzzle, 4))
#[1,3,4,6,7] - predicted result - check
print str(box_possibles(puzzle, 1, 1))
#[1,2,3,6,7,8,9] - predicted result - check
