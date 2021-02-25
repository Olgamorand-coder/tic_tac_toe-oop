from game.player.BasePlayer import BasePlayer
from copy import deepcopy

class HardPlayer(BasePlayer):
    def __init__(self, playerType, board):
        super().__init__(playerType, board)
        self.best_coord=None


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
                new_result=self.minimax("O", new_board)
                if new_result>result:
                    result=new_result
                    self.best_coord=move


            elif playerType=="O":
                new_result=self.minimax ("X", new_board)
                if new_result<result:
                    result=new_result
                    self.best_coord=move


        return result



    def make_move(self):
        board = super().get_board()
        player = super().get_player_type()
        x, y=self.best_coord

        board.update_cell(x, y, player)







