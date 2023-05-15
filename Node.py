class Node:
    def __init__(self, player):
        self.player = player
        self.next = None

    def get_next(self):
        return self.next