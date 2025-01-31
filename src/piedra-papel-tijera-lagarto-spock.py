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

