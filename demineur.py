import random

#affichage de la grille dans la console
def create_grid(rows, cols, value):
    """
        Function that creates the grid visible by the user.

        :param rows: the number of rows we want in the grid
        :type rows: int
        :param cols: the number of colomns we want in the grid
        :type cols: int
        :param value: What we want to display in each cell
        :type value: str
    """
    grid = []
    for i in range(rows):
        new_row = []
        for j in range(cols):
            new_row.append(value)
        grid.append(new_row)
    return grid

def get_neighbors(rows, cols, r, c):
    """
        Function to get the neighbors cells

        :param rows: The number of rows in our grid
        :type rows: int
        :params cols: the number of cols in our grid
        :type cols: int
        :params r: the number of the row
        :type r: int
        :params c: the number of the column
        :type c: int
        :return: a list with the coordinates of each neighbor
    """
    neighbors = []
    for i in range(-1,2,1):
        for j in range (-1,2,1):
            if (i !=0 or j!=0) and (r+i>=0 and c+j>=0) and (r+i<rows and c+j< cols):
                neighbors.append((r+i,c+j))
    return neighbors
    

def generate_mines(rows, cols, nb_mines, forbidden_cell):
    """
        function that generate where to place the mines randomly.
    """
    mines = []

    for i in range (0,nb_mines):
        pass
    
    pass

def create_hidden_grid(rows, cols, mines):
    pass

def reveal(hidden, visible, r, c):
    pass

def print_grid(grid):
    pass

def has_won(hidden, visible):
    pass

def minesweeper(rows, cols, nb_mines):
    pass