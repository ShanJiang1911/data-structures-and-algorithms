class Node:
  def __init__(self, value, left=None, right=None):
    self.value = value
    self.left = left
    self.right = right

def breadth_first(root):
    if root is None:
        return

    queue = []

    queue.append(root)

    while(len(queue) > 0):

        print(queue[0].value)
        node = queue.pop(0)

        if node.left is not None:
            queue.append(node.left)

        if node.right is not None:
            queue.append(node.right)
    return queue

#test
root = Node(1)
root.left = Node(3)
root.right = Node(5)
root.left.left = Node(7)
root.left.right = Node(9)
root.right.left = Node(11)
root.right.right = Node(13)


breadth_first(root)
