
class EmptyMoveException(Exception):
    def __init__(self):
        super().__init__("Player must make a move")
