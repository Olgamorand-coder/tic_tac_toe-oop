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

    def __is_coord_ok(self, coord_x, coord_y):
        if coord_y < 0 or coord_x < 0:
            return False
        elif coord_y >= len(self.cells[0]) or coord_x >= len(self.cells):
            return False

        return True


    # check if you can play selected coordinates
    def check_move(self, coord_x, coord_y):
        if not self.__is_coord_ok(coord_x, coord_y):
            raise IndexError

        return self.cells[coord_x][coord_y] == "_"


    def update_cell(self, coord_x, coord_y, player):
        if not self.__is_coord_ok(coord_x, coord_y):
            raise IndexError

        # check if coord are right
        if self.cells[coord_x][coord_y] == "_":
            self.cells[coord_x][coord_y] = player
        else:
            raise Exception

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
                return True
            elif self.is_draw() == False:
                return False
        else:
            return True

