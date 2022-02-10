# from tree.binary_tree import BinaryTree
# from tree.binary_search_tree import BinarySearchTree
# from tree.node import Node

# # Can successfully instantiate an empty tree
# def test_binary_tree_empty():
#   tree = BinaryTree()
#   assert tree

# # Can successfully instantiate a tree with a single root node
# def test_binary_tree_single_root():
#   orange = Node("orange")
#   tree = BinaryTree(orange)
#   actual = tree.root.value
#   expected = "orange"
#   assert actual == expected

# # Can successfully add a left child and right child to a single root node
# def test_add_left_right_child():
#   ten = Node(10)
#   bst = BinarySearchTree(ten)
#   bst.add(5)
#   bst.add(15)
#   assert bst.root.value == 10
#   assert bst.root.left.value == 5
#   assert bst.root.right.value == 15

# # Can successfully return a collection from a preorder traversal
# def test_pre_order():
#   pork = Node("pork")
#   pork.left = Node("chicken")
#   pork.right = Node("beef")

#   tree = BinaryTree(pork)
#   expected = ["pork", "chicken", "beef"]
#   actual = tree.pre_order()

#   assert actual == expected

# # Can successfully return a collection from an inorder traversal
# def test_in_order():
#   burger = Node("burger")
#   burger.left = Node("pizza")
#   burger.right = Node("wings")

#   tree = BinaryTree(burger)
#   expected = ["pizza", "burger", "wings"]
#   actual = tree.in_order()
#   assert actual == expected

# # Can successfully return a collection from a postorder traversal
# def test_post_order():
#   coke = Node("coke")
#   coke.left = Node("sprite")
#   coke.right = Node("mtd")

#   tree = BinaryTree(coke)
#   expected = ["sprite", "mtd", "coke"]
#   actual = tree.post_order()
#   assert actual == expected
