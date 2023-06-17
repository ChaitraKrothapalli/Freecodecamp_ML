import random

def player(prev_play, opponent_history=[]):
    # Check if it's the first game in a match
    if prev_play == "":
        return random.choice(["R", "P", "S"])
    
    # Determine opponent's last move
    opponent_last_play = opponent_history[-1]
    
    # Choose your next move based on opponent's last move
    if opponent_last_play == "R":
        return "P"  # Beat Rock with Paper
    elif opponent_last_play == "P":
        return "S"  # Beat Paper with Scissors
    else:
        return "R"  # Beat Scissors with Rock
