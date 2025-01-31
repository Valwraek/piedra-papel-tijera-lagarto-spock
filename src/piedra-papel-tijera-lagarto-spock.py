from enum import IntEnum

class Game_action(IntEnum):
    PIEDRA = 0
    PAPEL = 1
    TIJERA = 2
    LAGARTO = 3
    SPOCK = 4

class Game_result(IntEnum):
    DERROTA = 0
    VICTORIA = 1
    EMPATE = 2

class Juego:
    def __init__(self):
        self.victorias = {
            Game_action.PIEDRA: [Game_action.TIJERA, Game_action.LAGARTO],
            Game_action.PAPEL: [Game_action.PIEDRA, Game_action.SPOCK],
            Game_action.TIJERA: [Game_action.PAPEL, Game_action.LAGARTO],
            Game_action.LAGARTO: [Game_action.SPOCK, Game_action.PAPEL],
            Game_action.SPOCK: [Game_action.PIEDRA, Game_action.TIJERA]
        }
    