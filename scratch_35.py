from random import randint
class Board:
    def __init__(self):
        self.table="_________"
        first_row = [self.table[0], self.table[1], self.table[2]]
        second_row = [self.table[3], self.table[4], self.table[5]]
        third_row = [self.table[6], self.table[7], self.table[8]]
        self.cells = []
        self.cells.append(first_row)
        self.cells.append(second_row)
        self.cells.append(third_row)

    def display_table(self):
        print("---------\n|", self.cells[0][0], self.cells[0][1], self.cells[0][2], "|")
        print("|", self.cells[1][0], self.cells[1][1], self.cells[1][2], "|")
        print("|", self.cells[2][0], self.cells[2][1], self.cells[2][2], "|")
        print("---------")


    def update_cell(self, coord_x, coord_y, player):
        # check if coord are right
        if self.cells[coord_x][coord_y]==" ":
            self.cells[coord_x][coord_y]=player

    def winner(self):
        if self.cells[0][0] == self.cells[1][1] == self.cells[2][2] != "_":
            return self.cells[0][0]
        elif self.cells[0][2] == self.cells[1][1] == self.cells[2][0] != "_":
            return self.cells[0][2]
        for i in range(3):
            if self.cells[i][0] == self.cells[i][1] == self.cells[i][2] != "_":
                return (self.cells[i][0])
            elif self.cells[0][i] == self.cells[1][i] == self.cells[2][i] != "_":
                return (self.cells[0][i])
        return None

    def is_draw(self):
        for row in self.cells:
            for i in row:
                if i == "_":
                    return False
        return True

    def winner_or_draw(self):
        is_winner = self.winner()
        if is_winner == None:
            if self.is_draw() == True:
                print("Draw")
                return True
            elif self.is_draw() == False:
                return False
        else:
            print(is_winner, "wins")
            return True


board=Board()
board.display_table()


board.update_cell(0, 0, "X")

board.display_table()

if board.winner_or_draw() is True:
    break