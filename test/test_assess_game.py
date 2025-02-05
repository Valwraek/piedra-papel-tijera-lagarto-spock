import pytest
from src.piedra_papel_tijera_lagarto_spock import Game, Game_action, Game_result


@pytest.fixture
def game():
    setup_game = Game()
    return setup_game

@pytest.mark.draw
def test_draw(game):
    assert Game_result.TIE == game.assess_game(
        user_action=Game_action.SPOCK,
        computer_action=Game_action.SPOCK)

    assert Game_result.TIE == game.assess_game(
        user_action=Game_action.LIZARD,
        computer_action=Game_action.LIZARD)

    assert Game_result.TIE == game.assess_game(
        user_action=Game_action.ROCK,
        computer_action=Game_action.ROCK)

    assert Game_result.TIE == game.assess_game(
        user_action=Game_action.SCISSORS,
        computer_action=Game_action.SCISSORS)

    assert Game_result.TIE == game.assess_game(
        user_action=Game_action.PAPER,
        computer_action=Game_action.PAPER)


@pytest.mark.SPOCK
def test_SPOCK_loses(game):
    '''
    SPOCK pierde con LIZARD y PAPER 
    '''
    assert Game_result.VICTORY == game.assess_game(
        user_action=Game_action.PAPER,
        computer_action=Game_action.SPOCK)

    assert Game_result.VICTORY == game.assess_game(
        user_action=Game_action.LIZARD,
        computer_action=Game_action.SPOCK)


@pytest.mark.SPOCK
def test_SPOCK_wins(game):
    '''
    SPOCK gana a ROCK y SCISSORS 
    '''
    assert Game_result.DEFEAT == game.assess_game(
        user_action=Game_action.ROCK,
        computer_action=Game_action.SPOCK)

    assert Game_result.DEFEAT == game.assess_game(
        user_action=Game_action.SCISSORS,
        computer_action=Game_action.SPOCK)


@pytest.mark.LIZARD
def test_LIZARD_loses(game):
    '''
    LIZARD pierde con ROCK y SCISSORS 
    '''
    assert Game_result.VICTORY == game.assess_game(
        user_action=Game_action.ROCK,
        computer_action=Game_action.LIZARD)

    assert Game_result.VICTORY == game.assess_game(
        user_action=Game_action.SCISSORS,
        computer_action=Game_action.LIZARD)


@pytest.mark.LIZARD
def test_LIZARD_wins(game):
    '''
    LIZARD gana a SPOCK y PAPER 
    '''
    assert Game_result.DEFEAT == game.assess_game(
        user_action=Game_action.SPOCK,
        computer_action=Game_action.LIZARD)

    assert Game_result.DEFEAT == game.assess_game(
        user_action=Game_action.PAPER,
        computer_action=Game_action.LIZARD)

@pytest.mark.ROCK
def test_ROCK_loses(game):
    '''
    ROCK pierde con SPOCK y PAPER 
    '''
    assert Game_result.VICTORY == game.assess_game(
        user_action=Game_action.SPOCK,
        computer_action=Game_action.ROCK)

    assert Game_result.VICTORY == game.assess_game(
        user_action=Game_action.PAPER,
        computer_action=Game_action.ROCK)

@pytest.mark.ROCK
def test_ROCK_wins(game):
    '''
    ROCK gana a SCISSORS y LIZARD 
    '''
    assert Game_result.DEFEAT == game.assess_game(
        user_action=Game_action.SCISSORS,
        computer_action=Game_action.ROCK)

    assert Game_result.DEFEAT == game.assess_game(
        user_action=Game_action.LIZARD,
        computer_action=Game_action.ROCK)

@pytest.mark.PAPER
def test_PAPER_loses(game):
    '''
    PAPER pierde con SCISSORS y LIZARD 
    '''
    assert Game_result.VICTORY == game.assess_game(
        user_action=Game_action.SCISSORS,
        computer_action=Game_action.PAPER)

    assert Game_result.VICTORY == game.assess_game(
        user_action=Game_action.LIZARD,
        computer_action=Game_action.PAPER)

@pytest.mark.PAPER
def test_PAPER_wins(game):
    '''
    PAPER gana a ROCK y SPOCK 
    '''
    assert Game_result.DEFEAT == game.assess_game(
        user_action=Game_action.ROCK,
        computer_action=Game_action.PAPER)

    assert Game_result.DEFEAT == game.assess_game(
        user_action=Game_action.SPOCK,
        computer_action=Game_action.PAPER)

@pytest.mark.SCISSORS
def test_SCISSORS_loses(game):
    '''
    SCISSORS pierde con SPOCK y ROCK 
    '''
    assert Game_result.VICTORY == game.assess_game(
        user_action=Game_action.SPOCK,
        computer_action=Game_action.SCISSORS)

    assert Game_result.VICTORY == game.assess_game(
        user_action=Game_action.ROCK,
        computer_action=Game_action.SCISSORS)

@pytest.mark.SCISSORS
def test_SCISSORS_wins(game):
    '''
    SCISSORS gana a LIZARD y PAPER 
    '''
    assert Game_result.DEFEAT == game.assess_game(
        user_action=Game_action.LIZARD,
        computer_action=Game_action.SCISSORS)

    assert Game_result.DEFEAT == game.assess_game(
        user_action=Game_action.PAPER,
        computer_action=Game_action.SCISSORS)
