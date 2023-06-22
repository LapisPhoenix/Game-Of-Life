import os
import time
from board import Board


def main():
    size = input("Enter Board Size (only 1 number): ")
    try:
        size = int(size)
    except ValueError:
        raise ValueError("You must enter a number!")
    
    auto = input("Automatically Generate? (Y/N): ")

    if not auto.casefold() in ['y', 'n']:
        raise ValueError("You must either enter Y or N.") 
    
    board = Board((size, size))

    alive_cells = input("Enter the coordinates of the alive cells (x1,y1 x2,y2 ...): ")
    for cell_coords in alive_cells.split():
        x, y = map(int, cell_coords.split(","))
        try:
            board.change_cell((x, y))
        except ValueError:
            print(f"Invalid coordinates provided: {cell_coords}")
    
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        board.print_board()
        print("\n\n\n")
        print(f"Generation: {board.generation}")
        if auto == "y":
            time.sleep(1)
        else:
            try:
                input(f"ENTER for next generation.")
            except KeyboardInterrupt:
                os.system("cls" if os.name == "nt" else "clear")
                print("Thanks for playing!")
                print("Good Bye...")
                exit
        
        board.calculate_next_generation()




if __name__ == "__main__":
    main()