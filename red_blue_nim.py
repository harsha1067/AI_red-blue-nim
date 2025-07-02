import sys

# For alpha-beta pruning
max_value = sys.maxsize
min_value = -sys.maxsize
max_depth = 3000000  # Maximum recursion depth for minimax algorithm


class NimGame:
    def __init__(self, previous_state, is_computerturn, red_count, blue_count, depth):
        self.red_count = red_count       
        self.blue_count = blue_count    
        self.depth = depth               
        self.evaluation_score = 0        
        self.previous_state = previous_state  # Reference to the previous state for backtracking
        self.is_computerturn = is_computerturn  


def evaluation(game, mode):
    calculated_score = (game.red_count * 2 + game.blue_count * 3)  # Calculating score based on marble counts
    score_multiplier = -1 if mode == "misere" else 1               # Invert score for "misere" mode

    if (game.red_count + game.blue_count) % 2 == 1:
        game.evaluation_score = calculated_score * score_multiplier if game.is_computerturn else calculated_score * (-score_multiplier)
    else:
        game.evaluation_score = calculated_score * (-score_multiplier) if game.is_computerturn else calculated_score * score_multiplier
    return game


# Minimax function with alpha-beta pruning to find the optimal move
def minmax(game, alpha, beta, mode):
    # Check for terminal condition (no marbles left in any pile)
    if game.red_count * game.blue_count == 0:
        game_end_condition = True if mode == "standard" else False
        game.evaluation_score = game.red_count * 2 + game.blue_count * 3  # Final score points based on remaining marbles

        # Final score based on end condition and current player's turn
        if game.is_computerturn == game_end_condition:
            game.evaluation_score = -game.evaluation_score
        return game

    # Depth limit for minimax
    if max_depth == game.depth:
        game = evaluation(game, mode)
        if max_depth == 0:
            game.red_count = game.red_count - 1 if game.red_count < game.blue_count else game.red_count
            game.blue_count = game.blue_count - 1 if game.blue_count <= game.red_count else game.blue_count
        return game

    # Possible moves: removing one red or one blue marble
    recurrsive_moves = [
        NimGame(game, not game.is_computerturn, game.red_count - 1, game.blue_count, game.depth + 1),
        NimGame(game, not game.is_computerturn, game.red_count, game.blue_count - 1, game.depth + 1)
    ]

    # Initialize optimal move and best score
    optimal_move = recurrsive_moves[0]
    best_score = min_value if game.is_computerturn else max_value

    # Loop through each move and apply minimax recursively
    for move in recurrsive_moves:
        result = minmax(move, alpha, beta, mode)
        if game.is_computerturn:
            if result.evaluation_score > best_score:
                best_score = result.evaluation_score
                optimal_move = result
            alpha = max(alpha, best_score)
        else:
            if result.evaluation_score < best_score:
                best_score = result.evaluation_score
                optimal_move = result
            beta = min(beta, best_score)
        if beta <= alpha:
            break  

    game.evaluation_score = optimal_move.evaluation_score
    if game.previous_state is None:
        return optimal_move  
    return game


# Function to toggle the current player
def toggle_player(current_player):
    return 'human' if current_player == 'computer' else 'computer'


def end_game(mode, red_count, blue_count, current_player):
    print(f"Current State: Red - {red_count}, Blue - {blue_count}")
    if mode == "misere":
        current_player = toggle_player(current_player)  
    if current_player == 'human':
        print(f"Computer won with {2 * red_count + 3 * blue_count} points.")
    else:
        print(f"Human won with {2 * red_count + 3 * blue_count} points.")


if __name__ == "__main__":
    mode = "standard"                   # Default game mode is set to "standard" instead of 'misere'
    current_player = 'computer'         # Starting player
    red_count, blue_count = int(sys.argv[1]), int(sys.argv[2])  # Initial count of red and blue marbles

    for arg in range(3, len(sys.argv)):
        arg_value = sys.argv[arg]
        if arg_value.isdigit():
            max_depth = int(arg_value)  
        if arg_value == "misere":
            mode = "misere"            
        if arg_value == "human":
            current_player = "human"    

    print(f"Game Start: Red - {red_count}, Blue - {blue_count}")
    while red_count > 0 and blue_count > 0:
        print(f"Current State: Red - {red_count}, Blue - {blue_count}")
        if current_player == 'human':
            chosen_pile = input("Choose a pile (red or blue): ")
            marbles_to_remove = int(input("Choose the number of marbles to remove (1 or 2): "))
            if chosen_pile == "red" and 1 <= marbles_to_remove <= 2:
                red_count -= marbles_to_remove
            elif chosen_pile == "blue" and 1 <= marbles_to_remove <= 2:
                blue_count -= marbles_to_remove
            else:
                print("Invalid move! Please try again.")
                continue  # Repeat turn if invalid input
        else:
            best_move = minmax(NimGame(None, True, red_count, blue_count, 0), min_value, max_value, mode)
            chosen_color = "red" if best_move.red_count != red_count else "blue"
            marbles_removed = red_count - best_move.red_count if chosen_color == "red" else blue_count - best_move.blue_count
            print(f"Computer removed {marbles_removed} {chosen_color} marbles.")

            # Update marble count based on computer's move
            if chosen_color == "red":
                red_count -= marbles_removed
            else:
                blue_count -= marbles_removed

        current_player = toggle_player(current_player)  # Switch to the other player

    end_game(mode, red_count, blue_count, current_player)  
