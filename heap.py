class TreeNode:
    def __init__(self, item, left, right):
        self.item = item
        self.left = left
        self.right = right

class BinaryMaxHeap:
    def __init__(self):
        self.items = [None]
    
    def __len__(self):
        return self.items - 1

    def _percolate_up(self):
        cur = len(self)

        parent = cur // 2

    def _percolate_down(self, cur):
        loc = cur
        left = 2 * cur
        right = 2 * cur + 1

        if len(self) >= left and self.items[loc] < self.items[left]:
            loc=left
        if len(self) >= right and self.items[loc] < self.items[right]:
            loc=right
        if 


    def insert(self, k):
        self.append(k)
        self._percolate_up()

    def extract(self):
        root_node = self.items[1]
        self.items[-1] = self.items[1]
        self.items.pop()
        self._percolate_down(1)
        return root_node