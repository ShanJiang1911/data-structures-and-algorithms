from tree.node import Node

class BinaryTree:
  def __init__(self, root=None):
    self.root = root

  def pre_order(self):
  # root -> left -> right

    values = []

    def step(root):
      if root is None:
        return
      values.append(root.value)
      step(root.left)
      step(root.right)

    step(self.root)

    return values

  def in_order(self):
  # left -> root -> right

    values = []

    def step(root):
      if root is None:
        return

      step(root.left)
      values.append(root.value)
      step(root.right)

    step(self.root)

    return values

  def post_order(self):
  #left -> right -> root

    def step(root, values):
      if root is None:
        return

      step(root.left, values)
      step(root.right, values)
      values.append(root.value)

      return values

    return step(self.root, [])
