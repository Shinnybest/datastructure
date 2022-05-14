class Node:
    def __init__(self, item):
        self.item = item
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    # 전위 순회
    def preorder(self, n):
        if n!=None:
            print(n.item, " ", end="")
            if n.left:
                self.preorder(n.left)
            if n.right:
                self.preorder(n.right)

    # 중위 순회
    def inorder(self, n):
        if n!=None:
            if n.left:
                self.preorder(n.left)
            print(n.item, " ", end="")
            if n.right:
                self.preorder(n.right)

    # 후위 순회
    def postorder(self, n):
        if n!=None:
            if n.left:
                self.preorder(n.left)
            if n.right:
                self.preorder(n.right)
            print(n.item, " ", end="")

    # 레벨 순회
    def levelorder(self, root):
        q = []
        q.append(root)
        while q:
            t=q.pop(0)
            print(t.item, " ", end="")
            if t.left != None:
                q.append(t.left)
            if t.right != None:
                q.append(t.right)

    # 높이 구하기
    def height(self, root):
        if self.root is None:
            return 0

        return max(self.height(root.left), self.height(root.right)) + 1
        



tree = BinaryTree()
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)
node5 = Node(50)
node6 = Node(60)
node7 = Node(70)
node8 = Node(80)

tree.root = node1
node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5
node3.left = node6
node3.right = node7
node4.left = node8

print("전위순회")
tree.preorder(tree.root)
print("\n중위순회")
tree.inorder(tree.root)
print("\n후위순회")
tree.postorder(tree.root)