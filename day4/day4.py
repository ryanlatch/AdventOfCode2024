"""
word search 8 directions
"""
import re


with open("input.txt", "r") as file:
    # read the file and remove any make it a list of strings essentially making a grid
    grid = file.read().splitlines()

"""
direction vectors. Left number, vertical. Right number, horizontal. 
horizontal: right - (0, 1), left - (0, -1)
vertiacl: down - (1, 0), up - (-1, 0)
diagonal: D-right - (1, 1), D-left - (1, -1), U-right - (-1, 1), U-left - (-1, -1)
"""

directions = [(0, 1), (0, -1), (1, 0 ), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
# fuck this

# regex time
def horizontal(grid):
    total = 0
    for line in grid:
        total += len(re.findall("XMAS", line))
        total += len(re.findall("SAMX", line))
    return total

print(horizontal(grid)) ## WOOOOOO

# transpose the grid and run the horizontal function again lol
def vertical(grid): 
    # transpose the grid
    columns = []
    # iterate through each column index, i.e # ABC, A, then B 
    for col in range(len(grid[0])): # grid[0] just means the first string
        column = "" # init empty string for the column
        for row in grid:
            column += row[col] # append the row letter at column position to the string
        columns.append(column)
    total = horizontal(columns)
    return total

print(vertical(grid))

def diagonal_get(grid):
    diagonals = []
    rows = len(grid)
    cols = len(grid[0])

    for start in range(rows + cols -1): # iter over all starting points for diag
        diagonal = [] 
        for r in range(rows): # for each row
            c = start - r # calc the col index (c)
            if 0 <= c < cols: # append characters that are within the bounds
                diagonal.append(grid[r][c]) # append the char at the coord 
        diagonals.append("".join(diagonal)) # append a string of the diagonal as an entry in the list
    
    for start in range(-cols + 1, rows):
        diagonal = []
        for r in range(rows):
            c = r - start  
            if 0 <= c < cols:
                diagonal.append(grid[r][c])
        diagonals.append("".join(diagonal))


    return horizontal(diagonals)

print(diagonal_get(grid))

answer = horizontal(grid) + vertical(grid) + diagonal_get(grid)

print("answer: ", answer)
