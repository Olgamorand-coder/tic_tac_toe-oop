from game.player.BasePlayer import BasePlayer


class UserPlayer(BasePlayer):
    def __init__(self, playerType, board):
        super().__init__(playerType, board)

    def make_move(self):
        not_valid = True
        while not_valid:
            try:
                coordinates = input("Enter the coordinates: ")
                coordinates = [int(i) for i in coordinates.split()]
                x, y = coordinates[0] - 1, coordinates[1] - 1

                board = super().get_board()
                player = super().get_player_type()

                if board.check_move(x,y):
                    not_valid = False
                    board.update_cell(x, y, player)

            except ValueError:
                print("You should enter numbers!")
            except IndexError:
                print("Coordinates should be from 1 to 3!")