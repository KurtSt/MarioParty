import random

class Player:
    def __init__(self, name):
        self.name = name
        self.location = None

    def hide(self, locations):
        self.location = random.choice(locations)

class Seeker:
    def __init__(self, name):
        self.name = name

    def seek(self, locations):
        removed_location = random.choice(locations)
        return removed_location

class Game:
    def __init__(self, players, seeker):
        self.players = players
        self.seeker = seeker
        self.locations = ['Location 1', 'Location 2', 'Location 3', 'Location 4']
        self.rounds = 3

    def play(self):
        for round in range(self.rounds):
            # Hiding phase
            for player in self.players:
                player.hide(self.locations)

            # Seeking phase
            removed_location = self.seeker.seek(self.locations)
            self.locations.remove(removed_location)

            # Check who has been found
            for player in self.players:
                if player.location == removed_location:
                    self.players.remove(player)

            if not self.players:
                return 'seeker'

            # Adjust locations for next round
            self.locations = ['Location ' + str(i+1) for i in range(len(self.locations))]

        else:
            return 'hiders'

# Simulation
num_simulations = 1000000
seeker_wins = 0
hiders_wins = 0

for _ in range(num_simulations):
    players = [Player('Hider 1'), Player('Hider 2'), Player('Hider 3')]
    seeker = Seeker('Seeker')
    game = Game(players, seeker)
    winner = game.play()

    if winner == 'seeker':
        seeker_wins += 1
    elif winner == 'hiders':
        hiders_wins += 1

print(f'After {num_simulations} simulations:')
print(f'The seeker won {seeker_wins} times.')
print(f'The hiders won {hiders_wins} times.')
