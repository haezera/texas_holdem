import Node

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, player):
        newNode = Node(player)
        if (self.head):
            current = self.head
            while (current.next):
                current = current.next
            current.next = newNode
        else:
            self.head = newNode
