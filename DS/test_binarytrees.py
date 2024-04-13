import binarytree

tree = binarytree.BinaryTree()

#create own unsorted tree
tree.root = binarytree.Node(1)
tree.root.left = binarytree.Node(4)
tree.root.right = binarytree.Node(3)
tree.root.left.right = binarytree.Node(6)
tree.root.left.left = binarytree.Node(5)
tree.root.right.right = binarytree.Node(9)
tree.root.right.left = binarytree.Node(7)

# tree traversals
tree.preorder(tree.root)
print()
tree.inorder(tree.root)
print()
tree.postorder(tree.root)