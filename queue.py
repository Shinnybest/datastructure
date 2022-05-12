class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next


class Queue:
    def __init__(self):
        self.head = None

    def push(self, data):
        if self.head is None:
            self.head = Node(data, None)
        else:
            node = self.head
            while node.next:
                node = node.next

            node.next = Node(data, None)

    def pop(self):
        if self.is_empty():
            return None
        else:
            first_node = self.head
            self.head = self.head.next
            return first_node.data

    def is_empty(self):
        return self.head is None