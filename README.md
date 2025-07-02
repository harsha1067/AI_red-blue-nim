Version: Python 3.11.9

red_blue_nim.py:

NimGame class to represent each game state, storing the red and blue marble counts, depth in the game tree, and whether it's the computer's turn. The evaluation() function calculates a score based on the game mode and current marble counts, while minmax() recursively explores possible moves to find the optimal play, pruning unnecessary branches to improve efficiency. The toggle_player() function switches turns between human and computer, and end_game() determines the final score and declares the winner based on the selected game mode. The evaluation() function provides a score that represents the game state. - Standard Mode: A negative score is assigned based on remaining marbles to minimize the score when either pile is empty. - Misère mode: A positive score is assigned based on remaining marbles. The main game loop in __main__  user input and initiates the game, allowing the human and computer to take turns until the game ends.

In standard mode:

Endgame Conditions:
If either red or blue marbles reach zero, the computer loses if it's turn and wins otherwise.
If the maximum search depth is reached, the evaluation function predicts the winner based on the remaining marbles.
Winning Strategy:
There are two possible end states: (red=0, blue=1) or (red=1, blue=0).
If both piles have one marble and it's the computer's turn, it chooses red to win by 3 points in standard mode or blue to reduce the human's score in misère mode.
Even/Odd Strategy:
In standard mode, if the total number of marbles is even and it's the computer's turn, the computer loses.
If the total number of marbles is odd and it's the computer's turn, the computer wins.
Scoring:
The final score is 2 for the red winner or 3 for the blue winner in optimal play.
Otherwise, the score is calculated as (remaining_red * 2 + remaining_blue * 3).
Search Depth and Evaluation:
The search depth controls the depth of the minimax algorithm.
The evaluation function determines the score based on the total number of marbles and the current player.
Since at least one marble must remain in each pile at all times, the winner can be predicted based on the total number of marbles and the current player's turn.

Instead of using a depth-limited search to determine the winner, there are 2 conditions in that depth for each depth game state:
Standard Mode:
If the total number of marbles is odd (1), the current player wins.
If the total number of marbles is even (0), the other player wins.
Misère Mode:
If the total number of marbles is odd(1), the other player wins.
If the total number of marbles is even(0), the current player wins.

To run the code:

To start the game with 13 red marbles, 4 blue marbles, the standard version, the computer as the first player, and a search depth 

use the command: 
red_blue_nim.py <num-red> <num-blue> <version> <first-player> <depth>

Ex: python red_blue_nim.py 13 4 standard computer 4

    python red_blue_nim.py 10 3 misère human 5

--> <num-red> & <num-blue>: Number of red and blue marbles 
--> version: Specifies the game version. If not defined, 'standard' version is used by default. In this case, it is 'standard' version, where a player loses if they encounter an empty pile at their turn, whereas 'misère' version, it will be vice versa (when a player encounters an empty pile at their turn, then the player wins).
--> first-player: It indicates which player goes first, either 'computer' or 'human'. Default 'computer' is used, if not defined. 
--> depth: It sets the search depth for the Minmax algorithm.

Once the game starts, the computer and human players take turns until a pile is empty, with the winner based on the version and the state of the game.
