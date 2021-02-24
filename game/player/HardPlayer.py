from game.player.BasePlayer import BasePlayer
from copy import deepcopy

class HardPlayer(BasePlayer):
    def __init__(self, playerType, board):
        super().__init__(playerType, board)

    def minimax(self, playerType, b):

        avail_spots=b.empty_indexies()
        if b.is_draw():
            return 0
        elif b.winner()=="X":
            return 1
        elif b.winner()=="O":
            return -1

        if playerType=="X":
            result=-2
        else:
            result=2
        for move in avail_spots:
            new_board=deepcopy(b)
            new_board.update_cell(move[0], move[1], playerType)
            if playerType=="X":
                new_result=self.minimax("O", new_board)[0]
                if new_result>result:
                    result=new_result
                    coord=new_result[1]

            elif playerType=="O":
                new_result=self.minimax ("X", new_board)[0]
                if new_result<result:
                    result=new_result
                    coord=new_result[1]

        return result, coord

    def best_move(self, board, player_type):
        score, coord=self.minimax(board, player_type)
        return coord

    def make_move(self):
        board = super().get_board()
        player = super().get_player_type()
        best_move=self.best_move(board, player)
        if board.check_move(best_move[0], best_move[1]):
            board.update_cell(best_move[0], best_move[1], player)







