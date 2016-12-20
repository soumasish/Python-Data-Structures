class BST:
    def __init__(self):
        self.root = None
        self.size = 0

    def insert(self, item):
        self.root = self.insert_helper(item, self)
        return self.root

    def insert_helper(self, item, root):
        if root is None:
            p = Node(item)
            return p
        if item > self.root.data:
            self.root = self.insert_helper(item, root.right)
        else:
            self.root = self.insert_helper(item, root.left)
        return self.root

    def preorder(self):
        self.preorder_helper(self.root)

    def preorder_helper(self, root):
        if root is None:
            return
        self.preoder_helper(root.left)
        print(root.data, end= ' ')
        self.preorder_helper(root.right)


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.rigth = None