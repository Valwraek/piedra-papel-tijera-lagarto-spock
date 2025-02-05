from enum import IntEnum
import random
import survey

class Game_action(IntEnum):
    ROCK = 0
    PAPER = 1
    SCISSORS = 2
    LIZARD = 3
    SPOCK = 4
    
    def get_game_choice():
        return [f"{game_action.name}[{game_action.value}]" for game_action in Game_action]

class Game_result(IntEnum):
    DEFEAT = 0
    VICTORY = 1
    TIE = 2

class Game:
    def __init__(self):
        self.VICTORYs = {
            Game_action.ROCK: [Game_action.SCISSORS, Game_action.LIZARD],
            Game_action.PAPER: [Game_action.ROCK, Game_action.SPOCK],
            Game_action.SCISSORS: [Game_action.PAPER, Game_action.LIZARD],
            Game_action.LIZARD: [Game_action.SPOCK, Game_action.PAPER],
            Game_action.SPOCK: [Game_action.ROCK, Game_action.SCISSORS]
        }
    def assess_game(self, user_action, computer_action):
        if user_action == computer_action:
            return Game_result.TIE
        if computer_action in self.VICTORYs[user_action]:
            return Game_result.VICTORY
        return Game_result.DEFEAT
    def computer_action(self):
        computer_action = random.choice(list(Game_action))
        return computer_action
    def play(self):
        computer_action = self.computer_action()
        while True:
            
            user_action =  survey.routines.select('Selecciona con que quieres jugar: ', options=Game_action.get_game_choice())
            print(f"Tu elección: {Game_action(user_action).name}")
            print(f"La elección de la computadora: {computer_action.name}")
            result = self.assess_game(user_action, computer_action)
            survey.printers.text(f"Resultado: {Game_result(result).name}")
            user_want_to_play = survey.routines.inquire('Quieres seguir jugando? ')
            if not user_want_to_play:
                break
            
if __name__ == "__main__":
    Game().play()         
        