import random

def simulate_game(num_players=4, num_buttons=5):
    players = list(range(num_players))
    while len(players) > 1:
        poisoned_button = random.randint(0, num_buttons-1)
        for player in players:
            pressed_button = random.randint(0, num_buttons-1)
            if pressed_button == poisoned_button:
                players.remove(player)
                break
        else:  # if no player hits the poisoned button
            continue  # start the next round without eliminating anyone
    return players[0]  # return the winner

def simulate_games(num_games=10000000):
    wins = [0]*4
    for _ in range(num_games):
        winner = simulate_game()
        wins[winner] += 1
    return wins

print(simulate_games())
