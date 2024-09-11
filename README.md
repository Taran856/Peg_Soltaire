# Peg Solitaire Game in Python

Welcome to **Peg Solitaire**, a classic puzzle game brought to life with Python! This project is a console-based implementation of the well-known Peg Solitaire game where the goal is to clear the board of pegs, leaving only one. It offers multiple board configurations, customizable moves, and an interactive experience directly from the terminal.

## Introduction

**Peg Solitaire** is a single-player board game where you attempt to remove pegs by "jumping" one over another, much like checkers. The aim is to reduce the board to just one remaining peg. This Python implementation gives players the choice of several unique board layouts, and it guides players through making valid moves.

You can run the game in any Python environment, and it includes features like:
- Choosing from multiple board layouts.
- Input validation for selecting and moving pegs.
- Real-time board updates after each move.
- Winning and losing scenarios with clear feedback.

## Features

### Interactive Gameplay:
- Users can interactively choose pegs and their movement directions (Up, Down, Left, or Right).
- The game validates each move, ensuring that only legal jumps are performed.

### Multiple Board Layouts:
- Choose from four distinct board designs to test your strategy:
  - **Cross**
  - **Circle**
  - **Triangle**
  - **Simple T**

### Game Outcome:
- You win when only one peg is left on the board.
- If no legal moves are left but more than one peg remains, you lose and can try again.

### Error Handling:
- Handles invalid inputs for selecting pegs, board types, and directions.
- Ensures that players only make valid moves.

## How to Play

1. Run the script.
2. Choose from four board layouts by entering the corresponding number.
3. Select a peg by specifying its row and column position.
4. Choose the direction to move the peg: Up (1), Down (2), Left (3), or Right (4).
5. The game updates the board with each valid move, and the process repeats until only one peg remains or no valid moves are left.

## Code Overview

The game logic is built around key functions that manage board setup, movement validation, and game state checks.

### Main Functions

- **`convert_strings_to_list(board)`**  
  Converts a string representation of the board into a list, making it easier to manipulate for gameplay.
  
- **`is_valid_move(board, row, column, direction)`**  
  Determines if a selected peg can be legally moved in the chosen direction. The function checks if the peg is jumping over another peg into an empty space.

- **`perform_move(board, row, column, direction)`**  
  Executes a valid move by updating the board state, replacing the peg positions.

- **`count_pegs_remaining(board)`**  
  Counts how many pegs are still present on the board.

- **`count_moves_available(board)`**  
  Returns the number of valid moves remaining based on the current board configuration.

- **`direction_in_words(direction)`**  
  Converts a numerical direction input into a human-readable string (e.g., "UP", "DOWN", "LEFT", "RIGHT").

### Core Game Loop

The game runs in a loop that continually prompts the user for input, checks for valid moves, and updates the board. It concludes when either the player wins (1 peg remaining) or no more legal moves can be made.

## Boards Available

You can choose from four different board layouts:

1. **Cross Board**
    ```
    ###@@@###
    ###@@@###
    @@@@@@@@@
    @@@@-@@@@
    @@@@@@@@@
    ###@@@###
    ###@@@###
    ```
   
2. **Circle Board**
    ```
    #-@@-#
    -@@@@-
    @@@@@@
    @@@@@@
    -@@@@-
    #-@@-#
    ```
   
3. **Triangle Board**
    ```
    ###-@-###
    ##-@@@-##
    #-@@-@@-#
    -@@@@@@@-
    ```
   
4. **Simple T Board**
    ```
    -----
    -@@@-
    --@--
    --@--
    -----
    ```

## Requirements

To run this game, you'll need:
- **Python 3.x**

No additional libraries are required; the game uses standard Python functionality.

## Running the Game

1. Clone the repository or download the script to your local machine.
2. Open a terminal and navigate to the folder containing the script.
3. Run the game with the following command:

    ```bash
    python peg_solitaire.py
    ```

4. Follow the on-screen prompts to choose a board and start playing!

## Example Gameplay

Here’s a quick example of how the game plays:

```plaintext
WELCOME TO PEG SOLITAIRE!
===============================

Board Style Menu
    1) Cross
    2) Circle
    3) Triangle
    4) Simple T

Choose a board style: 1
###@@@###
###@@@###
@@@@@@@@@
@@@@-@@@@
@@@@@@@@@
###@@@###
###@@@###

Choose the COLUMN of a peg you'd like to move: 4
Choose the ROW of a peg you'd like to move: 4
Choose a DIRECTION to move that peg 1) UP, 2) DOWN, 3) LEFT, or 4) RIGHT: 1
###@@@###
###@@@###
@@@@@@@@@
@@@--@@@@
@@@@@@@@@
###@@@###
###@@@###
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributions

Feel free to submit issues or pull requests if you have any improvements or bug fixes!

## Screenshots

_Note: Add your screenshots here once you've run the game._
