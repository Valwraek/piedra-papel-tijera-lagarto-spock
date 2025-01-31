from enum import IntEnum

class Game_action(IntEnum):
    ROCK = 0
    PAPER = 1
    SCISSORS = 2
    LIZARD = 3
    SPOCK = 4

class Game_result(IntEnum):
    DERROTA = 0
    VICTORIA = 1
    EMPATE = 2

class Juego:
    def __init__(self):
        self.victorias = {
            Game_action.ROCK: [Game_action.SCISSORS, Game_action.LIZARD],
            Game_action.PAPER: [Game_action.ROCK, Game_action.SPOCK],
            Game_action.SCISSORS: [Game_action.PAPER, Game_action.LIZARD],
            Game_action.LIZARD: [Game_action.SPOCK, Game_action.PAPER],
            Game_action.SPOCK: [Game_action.ROCK, Game_action.SCISSORS]
        }
    def assess_game(self, user_action, computer_action):
        if user_action == computer_action:
            return Game_result.EMPATE
        if computer_action in self.victorias[user_action]:
            return Game_result.VICTORIA
        return Game_result.DERROTA
    