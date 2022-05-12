class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = Node(data)
        new_node.prev = self.top
        self.top = new_node

    def pop(self):
        top_node = self.top.data
        if self.is_empty():
            return None
        else:
            self.top = self.top.prev
            return top_node

    def is_empty(self):
        if self.top is None:
            return True
        return False