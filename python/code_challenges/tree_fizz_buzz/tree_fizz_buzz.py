class Node:
  def __init__(self, value=None):
    self.value = value
    self.childen = []

class KaryTree:
  def __init__(self, root=None):
    self.root = root

  def add(self, value):
    if self.root is None:
      self.root = Node(value)
    else:
      self.root.childen.append(Node(value))

def fizz_buzz_tree(tree):
  KaryTreeList = []
  newKaryTreeList = []

  for i in KaryTreeList:
    if i.value % 3 == 0:
      i = "Fizz"
    elif i.value % 5 == 0:
      i = "Buzz"
    elif i.value % 3 == 0 and i.value % 5 == 0:
      i = "FizzBuzz"
    else:
      i = str(i)
    newKaryTreeList.append(i)
  return newKaryTreeList



