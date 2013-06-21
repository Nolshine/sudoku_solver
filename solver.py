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


def row_possibles(puzzle, row):
    #start with a fresh possible range
    possibles = [1,2,3,4,5,6,7,8,9]
    structure = puzzle[row]
    
    for cell in structure:
        print str(possibles)
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
        print str(structure)
    print "--------------------"
    for cell in structure:
        if cell != 0:
            if cell in possibles:
                possibles.remove(cell)
    return possibles



print str(row_possibles(puzzle, 0))
#this should print out [1,2,3,5,6,7,8]
print str(col_possibles(puzzle, 0))
#this should print out [1,2,3,4,5,6,7]
