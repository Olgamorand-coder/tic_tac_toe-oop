from game.player.BasePlayer import BasePlayer
from random import randint

import copy


class MediumPlayer(BasePlayer):

    def __init__(self, playerType, board):
        super().__init__(playerType, board)


    def define_adversary(self):
        adversary=""
        if super().get_player_type()=="X":
            adversary="O"
        elif super().get_player_type()=="O":
            adversary="X"
        return adversary

    def winning_prediction(self):
        board=super().get_board()
        player = super().get_player_type()


        winning_list=[]


        for row in range (len(board.cells)):
            for col in range (len(board.cells[row])):
                board_copy = copy.deepcopy(self.board)
                if board_copy.check_move(row, col):
                    board_copy.update_cell(row, col, player)
                    if board_copy.winner()==player:
                        winning_list.append(row)
                        winning_list.append(col)

        return winning_list

    def block_prediction(self):
        board = super().get_board()
        enemy=self.define_adversary()

        block_list=[]
        for row in range(len(board.cells)):
            for col in range (len(board.cells[row])):
                board_copy = copy.deepcopy(self.board)
                if board_copy.check_move(row, col):
                    board_copy.update_cell(row, col, enemy)
                    if board_copy.winner() ==enemy:
                        block_list.append(row)
                        block_list.append(col)
        return block_list

    def make_move(self):
        board = super().get_board()
        win_list=self.winning_prediction()
        block_list=self.block_prediction()
        player = super().get_player_type()

        if len(win_list)!=0:
            x = win_list[0]
            y = win_list[1]
            if board.check_move(x, y):
                board.update_cell(x, y, player)
        elif len(block_list)!=0:
            x = block_list[0]
            y = block_list[1]
            if board.check_move(x, y):
                board.update_cell(x, y, player)
        else:
            not_valid = True
            while not_valid:
                x = randint(0, 2)
                y = randint(0, 2)
                if board.check_move(x, y):
                    board.update_cell(x, y, player)
                    not_valid = False
 #how to replace the last part with EasyPlayer move?


