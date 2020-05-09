class TreeNode:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self._root = None
    
    def find(self, value):
        node = self._root
        while node and node.data != value:
            node = node.left if node.data > value else node.right
        return node
    
    def insert(self, value):
        if not self._root:
            self._root = TreeNode(value)
            return
        parent = None
        node = self._root
        while node:
            parent = node
            node = node.left if node.data > value else node.right
        newnode = TreeNode(value)
        if value > parent.data:
            parent.right = newnode
        else:
            parent.left = newnode
    
    def delete(self, value):
        node = self._root
        parent = None
        while node and node.data != value:
            parent = node
            node = node.left if node.data > value else node.right
        if node.left and node.right:
            successor = node.right
            successor_parent = node
            while successor.left:
                successor_parent = successor
                successor = successor.left
            node.data = successor.data
            parent, node, = successor_parent, successor

        child = node.left if node.left else node.right
        if not parent:
            self._root = child
        elif parent.left == node:
            parent.left = child
        else:
            parent.right = child