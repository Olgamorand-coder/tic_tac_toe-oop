class TicTacToeGame:
    def __init__(self, board, playerX, playerO):
        #if playerX.get_player_type() != "X":
            #raise Exception
        #if playerO.get_player_type() != "O":
            #raise Exception

        self.board = board
        self.playerX = playerX
        self.playerO = playerO

    def play(self):
        next_player = self.playerX

        while not self.board.winner_or_draw():
            next_player.make_move()
            next_player = self.__invert_player(next_player)
            self.board.display_table()

        if self.board.is_draw():
            print("Draw")
        elif self.board.winner() == "X":
            print("X wins")
        elif self.board.winner() == "O":
            print("O wins")

    def __invert_player(self, player):
        if player.get_player_type() == "X":
            return self.playerO
        if player.get_player_type() == "O":
            return self.playerX


