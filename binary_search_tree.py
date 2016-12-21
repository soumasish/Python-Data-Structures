class BST:
    def __init__(self):
        self.root = None
        self.size = 0

    def insert(self, item):
        self.root = self.insert_helper(item, self.root)
        self.size += 1
        return self.root

    def insert_helper(self, item, root):
        if root is None:
            p = Node(item)
            root = p
            return root
        if item > root.data:
            root.right = self.insert_helper(item, root.right)
        else:
            root.left = self.insert_helper(item, root.left)
        return root

    def preorder(self):
        self.preorder_helper(self.root)

    def preorder_helper(self, root):
        if root is None:
            return
        print(root.data, end=' ')
        self.preorder_helper(root.left)
        self.preorder_helper(root.right)

    def postorder(self):
        self.postorder_helper(self, self.root)

    def postorder_helper(self, root):
        if root is None:
            return




class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None