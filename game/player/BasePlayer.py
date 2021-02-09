from game.player.exceptions.EmptyMoveException import EmptyMoveException


class BasePlayer:
    def __init__(self, playerType, board):
        self.playerType = playerType
        self.board = board

    def get_board(self):
        return self.board

    def get_player_type(self):
        return self.playerType

    # make move in tic-tac-toe using board info and player type
    def make_move(self):
        raise EmptyMoveException
