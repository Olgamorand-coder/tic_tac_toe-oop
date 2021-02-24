from game.Board import Board
from game.TicTacToeGame import TicTacToeGame
from game.player.EasyPlayer import EasyPlayer
from game.player.UserPlayer import UserPlayer
from game.player.medium_player import MediumPlayer
from game.player.HardPlayer import HardPlayer


def check_input(some_input):
    possible_input = ["user", "easy", "medium", "hard"]
    try:
        g_mode = some_input.split()
        if len(g_mode) == 1 and g_mode[0] == "exit":
            return "exit"
        elif len(g_mode) == 3 and g_mode[0] == "start" and g_mode[1] in possible_input and g_mode[2] in possible_input:
            return "start"
    except TypeError:
        print("Bad parameters!")


def parse_input(some_input):
    some_input = some_input.split()
    x, o = some_input[1], some_input[2]
    return x, o


def build_player(player_class, player_type, board):
    if player_class == "user":
        return UserPlayer(player_type, board)
    if player_class == "easy":
        return EasyPlayer(player_type, board)
    if player_class=="medium":
        return MediumPlayer(player_type, board)
    elif player_class=="hard":
        return HardPlayer


def main():
    not_quit = True
    while not_quit:
        menu_input = input()
        board = Board()
        board.display_table()

        if check_input(menu_input) == "exit":
            not_quit = False
        if check_input(menu_input) == "start":
            pX, pO = parse_input(menu_input)

            pX = build_player(pX, "X", board)
            pO = build_player(pO, "O", board)

            game = TicTacToeGame(board, pX, pO)
            game.play()

        else:
            print("Bad parameters!")


main()

