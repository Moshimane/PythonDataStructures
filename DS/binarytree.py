class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
        
        
class BinaryTree:
    def __init__(self):
        self.root = None
        
    def add_child(self, root, data):
        if root is not None:
            if root.data < data:
                if root.right is None:
                    root.right = Node(data)
                else:
                    self.add_child(root.right, data)
            else:
                if root.left is None:
                    root.left = Node(data)
                else:
                    self.add_child(root.left, data)
        else:
            self.root = Node(data)
                  
    def inorder(self, root):
        if root is not None:
            self.inorder(root.left)
            print(root.data, end=' ')
            self.inorder(root.right)
        
    def preorder(self, root):
        if root is not None:
            print(root.data, end=' ')
            self.inorder(root.left)
            self.inorder(root.right)
        
    def postorder(self, root):
        if root is not None:
            self.inorder(root.left)
            self.inorder(root.right)
            print(root.data, end=' ')