class Cell:
    def __init__(self, state: str = "dead", position: tuple[int, int] = None):
        """ A single cell in Conway's Game of Life.
        
        # Args
        - state:     str             = The state of the cell, either 'dead' or 'alive'.
        - position: tuple[int, int] = The position of the cell, an X and Y value.

        # Raises
        - ValueError

        # Methods
        - get_current_state     = Gets the current state of the cell
        - get_x_position        = Gets the current X position
        - get_y_position        = Gets the current Y position
        - get_current_position  = Gets the current position with both X and Y in a tuple
        - change_state          = Changes the current state of the cell, either to a specified state or the opposite of the current state 
        """
        self.state = state.casefold()
        self.position = position

        self._check_position_validity(self.position)
        self._check_state_validity(self.state)

    def __repr__(self) -> str:
        return f"Cell: State: {self.state}, Position: X: {self.position[0]}, Y: {self.position[1]}"

    def __str__(self) -> str:
        return f"Cell: State: {self.state}, Position: X: {self.position[0]}, Y: {self.position[1]}"
    
    def _check_position_validity(self, position: tuple[int, int] = None) -> None:
        if position is None:
            position = self.position

        if not isinstance(position, tuple):
            raise ValueError(f"Cell Position must be a tuple, not {type(position)}")

        if len(position) != 2:
            raise ValueError("Cell Position must have two elements: X and Y")

        x, y = position
        if not all(isinstance(coord, int) for coord in (x, y)):
            raise ValueError(f"X and Y Position of the Cell must be integers, not {type(x)}, {type(y)}")

    def _check_state_validity(self, state: str = None) -> None:
        if state is None:
            state = self.state

        if not isinstance(state, str):
            raise ValueError(f"Cell State must be a string, not {type(state)}")

        if state not in ["dead", "alive"]:
            raise ValueError(f"Cell State must be either 'dead' or 'alive', not {state}")
    
    def get_current_state(self) -> str:
        """Gets the current state of the cell"""
        return self.state
    
    def get_x_position(self) -> int:
        """Gets the current X position"""
        return self.position[0]
    
    def get_y_position(self) -> int:
        """Gets the current Y position"""
        return self.position[1]
    
    def get_current_position(self) -> tuple[int, int]:
        """Gets the current position with both X and Y in a tuple"""
        return self.position
    
    def change_state(self, state: str = None) -> None:
        """Changes the current state of the cell, either to a specified state or the opposite of the current state"""
        if state is None:
            state = self.state
        
            self._check_state_validity(state)

            if state == "dead":
                self.state = "alive"
            else:
                self.state = "dead"
        else:
            self._check_state_validity(state)
            self.state = state