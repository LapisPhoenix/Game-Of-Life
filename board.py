from cell import Cell


class Board:
    def __init__(self, size: tuple[int, int]):
        """ The entire board for the game of life
        # Args
        - size: tuple[int, int] = The size of the board, they must be the same number. EX (10, 10)

        # Raises
        - ValueError

        # Methods
        get_x_size                  = Gets the x size of the board
        get_y_size                  = Gets the y size of the board
        get_board_size              = Gets the size of the board in a tuple
        get_grid                    = Gets the entire Grid
        get_number_of_cells         = Gets the total number of cells.
        access_cell_directly        = Gets the cell directly and returns it.
        change_cell                 = Changes the cell's state at a given coordinate
        print_board                 = Prints the current state of the board
        calculate_next_generation   = Generates the next generation of the board
        """
        self.size = size
        self.grid = [[Cell(position=(x, y)) for x in range(size[1])] for y in range(size[0])]
        self._check_size_validity(self.size)
        self.alive_symbol = "@"
        self.dead_symbol = "+"
        self.generation = 0
    
    def _check_size_validity(self, size: tuple[int, int] = None) -> None:
        if size is None:
            size = self.size
        
        x, y = size
        
        if not isinstance(size, tuple):
            raise ValueError(f"Board Size must be a tuple, not {type(size)}")
        elif len(size) != 2:
            raise ValueError(f"Board must be composed of an X and Y")
        elif not all(isinstance(side, int) for side in (x, y)):
            raise ValueError(f"X and Y size must be integers, not {type(x)}, {type(y)}")
        elif x <= 0 or y <= 0:
            raise ValueError(f"Board Size must be positive!")
        elif x != y:
            raise ValueError(f"Board Size must be a square, not {x}, {y}")
    
    def get_x_size(self) -> int:
        """Gets the x size of the board"""
        return self.size[0]
    
    def get_y_size(self) -> int:
        """Gets the y size of the board"""
        return self.size[1]
    
    def get_board_size(self) -> tuple[int, int]:
        """Gets the size of the board in a tuple"""
        return self.size
    
    def get_grid(self) -> list:
        """Gets the entire Grid"""
        return self.grid
    
    def get_number_of_cells(self) -> int:
        """Gets the total number of cells."""
        return self.get_x_size() * self.get_y_size()
    
    def access_cell_directly(self, coords: tuple[int, int]):
        """Gets the cell directly and returns it."""
        x, y = coords
        if 0 <= x < self.get_x_size() and 0 <= y < self.get_y_size():
            return self.grid[y][x]
        else:
            raise ValueError("Invalid coordinates provided.")

    def change_cell(self, coords: tuple[int, int]):
        """Changes the cell's state at a given coordinate"""
        x, y = coords
        x = max(0, x - 1)
        y = max(0, y - 1)
        if 0 <= x < self.get_x_size() and 0 <= y < self.get_y_size():
            cell = self.grid[y][x]
            cell.change_state()
        else:
            raise ValueError("Invalid coordinates provided.")
    
    def print_board(self):
        """Prints the current state of the board"""
        for row in self.grid:
            row_string = ""
            for cell in row:
                row_string += self.alive_symbol if cell.get_current_state() == "alive" else self.dead_symbol
            print(row_string)

    def calculate_next_generation(self):
        """Generates the next generation of the board"""
        new_grid = [[Cell(position=(x, y)) for x in range(self.get_x_size())] for y in range(self.get_y_size())]

        for y in range(self.get_y_size()):
            for x in range(self.get_x_size()):
                cell = self.grid[y][x]
                new_cell = new_grid[y][x]
                live_neighbor_count = self.count_live_neighbors(x, y)

                if cell.get_current_state() == "alive":
                    if live_neighbor_count < 2 or live_neighbor_count > 3:
                        new_cell.change_state("dead")
                    else:
                        new_cell.change_state("alive")
                else:
                    if live_neighbor_count == 3:
                        new_cell.change_state("alive")
                    else:
                        new_cell.change_state("dead")
        
        self.generation += 1
        self.grid = new_grid

    def count_live_neighbors(self, x: int, y: int) -> int:
        """Counts the number of live neighbors for a given cell at coordinates (x, y)"""
        live_count = 0
        for i in range(max(0, x-1), min(x+2, self.get_x_size())):
            for j in range(max(0, y-1), min(y+2, self.get_y_size())):
                if (i, j) != (x, y) and self.grid[j][i].get_current_state() == "alive":
                    live_count += 1
        return live_count