import random
from collections import Counter

# Define possible directions
directions = ['up', 'down', 'left', 'right', 'straight']

# Counter to keep track of wins
win_counter = Counter()

# Run the simulation for 1 million games
for _ in range(1000000):
    team = [0, 0, 0]  # Initialize team, 0 means active, 1 means eliminated
    for _ in range(5):  # Each game lasts for 5 rounds
        solo_move = random.choice(directions)  # Solo player makes a move

        # Team players make their moves
        team_moves = [random.choice(directions) if team[i] == 0 else 'eliminated' for i in range(3)]

        # Check if any team player matches the solo player
        for i in range(3):
            if team_moves[i] == solo_move:
                team[i] = 1  # The player is eliminated

        # If all team players are eliminated, the solo player wins
        if sum(team) == 3:
            win_counter['solo'] += 1
            break
    else:  # This else clause corresponds to the for-loop, it runs when the loop finishes normally (no break)
        win_counter['team'] += 1  # If the game lasts for 5 rounds, the team wins

print(win_counter)
