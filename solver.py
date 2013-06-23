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
    possibles = [1,2,3,4,5,6,7,8,9]
    structure = puzzle[row]
    
    for cell in structure:
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
    row = (row/3)
    column = (column/3)
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

def cell_possibles(puzzle, row, column):
    #function for determining what can be put in a cell
    cell_value = puzzle[row][column]
    #if the cell is full, nothing is possible in in
    if cell_value != 0:
        return 0
    else:
        cell_poss = [1,2,3,4,5,6,7,8,9]
        not_poss = []
        row_poss = row_possibles(puzzle, row)
        col_poss = col_possibles(puzzle, column)
        box_poss = box_possibles(puzzle, row, column)
        for i in range(1,10):
            if i not in row_poss:
                if i not in not_poss:
                    not_poss.append(i)
            if i not in col_poss:
                if i not in not_poss:
                    not_poss.append(i)
            if i not in box_poss:
                if i not in not_poss:
                    not_poss.append(i)
        for i in not_poss:
            cell_poss.remove(i)
            
        return cell_poss


print str(cell_possibles(puzzle, 7, 4))
#[1,3,7] - predicted result - check
print str(cell_possibles(puzzle, 1, 0))
#0 - predicted result - check
print str(cell_possibles(puzzle, 2, 0))
#[3,4,5] - predicted result - check
print str(cell_possibles(puzzle, 8, 8))
#[2,3,5,6,9] - predicted result - check
