from game.player.BasePlayer import BasePlayer
from random import randint


class EasyPlayer(BasePlayer):
    def __init__(self, playerType, board):
        super().__init__(playerType, board)

    def make_move(self):
        not_valid = True
        while not_valid:
            x = randint(0, 2)
            y = randint(0, 2)

            board = super().get_board()
            player = super().get_player_type()

            if board.check_move(x, y):
                board.update_cell(x, y, player)
                not_valid = False