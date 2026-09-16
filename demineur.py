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
        :return: The created grid
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
    neighbors = set()
    for i in range(-1,2,1):
        for j in range (-1,2,1):
            if (i !=0 or j!=0) and (r+i>=0 and c+j>=0) and (r+i<rows and c+j< cols):
                neighbors.add((r+i,c+j))
    return neighbors
    

def generate_mines(rows, cols, nb_mines, forbidden_cell):
    """
        function that places the mines randomly.

        :param rows: the number of rows in our grid
        :type rows: int
        :param cols: the number of columns in our grid
        :type cols: int
        :param nb_mines: the number of mines we want to put on our grid
        :type nb_mines: int
        :param forbidden_cell: A specified cell that cannot be a mine
        :type forbidden_cell: a tuple with coordinates
        :return: a Tuple containing the coordinates of all the mines
    """
    mines = set()
    while(len(mines)<nb_mines):
        new_mine = (random.randint(0,rows-1),random.randint(0,cols-1))
        if new_mine != forbidden_cell:
            mines.add(new_mine)
    return mines

def create_hidden_grid(rows, cols, mines):
    """
        Function that create a grid, invisible to the user, where all the mines and numbers are written

        :param rows: the number of rows on our grid
        :type rows: int
        :param cols: the number of columns on our grid
        :type cols: int
        :param mines: the tuple containing the coordinates of the mines
        :type mines: tuple containing tuples of coordinates
        :return: the list containing all the answers
    """
    hidden_grid = create_grid(rows,cols,0)

    for coord in mines:
        hidden_grid[coord[0]][coord[1]] = "*"

    for i in range (rows):
        for j in range(cols):
            if (i,j) not in mines:
                neighbors = get_neighbors(rows, cols, i, j)
                hidden_grid[i][j]= len(neighbors.intersection(mines))

    return hidden_grid


def reveal(hidden, visible, r, c):
    """
        Function that reaveal a case on click. if 0, reveals also the neighbors that are 0.

        :param hidden: the List of all the cells with the solutions, hidden to the user.
        :type hidden: List
        :param visible: the List of all the cells displayed to the user.
        :type visible: List
        :param r: the index of the row clicked by the user
        :type r: int
        :param c: the index of the column clicked by the user
        :type c: int
    """
    if visible[r][c] != "?":
        return

    visible[r][c] = hidden[r][c]
    pass

    if hidden[r][c] == "*":
        return
    elif hidden[r][c] != 0:
        return

    neighbors = get_neighbors(len(hidden),len(hidden[0]),r,c)
    for neighbor in neighbors:
        reveal(hidden,visible,neighbor[0],neighbor[1])


def print_grid(grid):
    """
        Function to display the grid in the console.

        :param grid: The grid to display
        :type grid: List[List[str]]
        :return: None
    """
    for row in grid :
        print(" ".join(str(cell) for cell in row))

def has_won(hidden, visible):
    """
        Function that returns True if all the non-mined cells are revealed.

        :param hidden: The grid containing the solutions, hidden to the user.
        :type hidden: List[List[str]]
        :param visible: The grid displayed to the user in the console
        :type visible: List[List[str]]
        :return: bool
    """
    for i in range(len(hidden)):
        for j in range(len(hidden[0])):
            if visible[i][j] == "?" and hidden[i][j] != "*":
                return False

    return True

def minesweeper(rows, cols, nb_mines):
    """
        Function to start a game of minesweeper
    """
    visible = create_grid(rows, cols, "?")
    hidden = None
    game_on = True

    while game_on :
        print_grid(visible)

        print("Commandes :")
        print("o ligne colonne → ouvrir une case")
        print("f ligne colonne → poser/retirer un drapeau")
        command = input("> ")

        parts = command.split()

        action = parts[0]
        r = int(parts[1])
        c = int(parts[2])
        
        if action == "o":
            if hidden is None:
                mines = generate_mines(rows,cols,nb_mines,(r,c))
                hidden = create_hidden_grid(rows,cols,mines)
            reveal(hidden,visible,r,c)

            if hidden[r][c] == "*":
                print("Perdu !")
                print_grid(hidden)
                game_on=False
            if has_won(hidden, visible):
                print("Gagné !")
                game_on = False
        else :
            if visible[r][c] == "?":
                visible[r][c] = "F"
            elif visible[r][c] == "F":
                visible[r][c] = "?"

minesweeper(3,4,3)