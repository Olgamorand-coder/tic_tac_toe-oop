class Board:
    def __init__(self):
        self.table="_________"
        first_row = [self.table[0], self.table[1], self.table[2]]
        second_row = [self.table[3], self.table[4], self.table[5]]
        third_row = [self.table[6], self.table[7], self.table[8]]
        self.__cells = []
        self.__cells.append(first_row)
        self.__cells.append(second_row)
        self.__cells.append(third_row)

    def display_table(self):
        print("---------\n|", self.__cells[0][0], self.__cells[0][1], self.__cells[0][2], "|")
        print("|", self.__cells[1][0], self.__cells[1][1], self.__cells[1][2], "|")
        print("|", self.__cells[2][0], self.__cells[2][1], self.__cells[2][2], "|")
        print("---------")

    def __is_coord_ok(self, coord_x, coord_y):
        if coord_y < 0 or coord_x < 0:
            return False
        elif coord_y >= len(self.__cells[0]) or coord_x >= len(self.__cells):
            return False

        return True


    # check if you can play selected coordinates
    def check_move(self, coord_x, coord_y):
        if not self.__is_coord_ok(coord_x, coord_y):
            raise IndexError

        return self.__cells[coord_x][coord_y] == "_"

    def update_cell(self, coord_x, coord_y, player):
        if not self.__is_coord_ok(coord_x, coord_y):
            raise IndexError

        # check if coord are right
        if self.__cells[coord_x][coord_y] == "_":
            self.__cells[coord_x][coord_y] = player
        else:
            raise Exception

    def winner(self):
        if self.__cells[0][0] == self.__cells[1][1] == self.__cells[2][2] != "_":
            return self.__cells[0][0]
        elif self.__cells[0][2] == self.__cells[1][1] == self.__cells[2][0] != "_":
            return self.__cells[0][2]
        for i in range(3):
            if self.__cells[i][0] == self.__cells[i][1] == self.__cells[i][2] != "_":
                return (self.__cells[i][0])
            elif self.__cells[0][i] == self.__cells[1][i] == self.__cells[2][i] != "_":
                return (self.__cells[0][i])
        return None

    def is_draw(self):
        for row in self.__cells:
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