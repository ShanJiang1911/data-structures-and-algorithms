class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

class LinkedList:
  def __init__(self):
    self.head = None

  def insert(self, value):
    # node = Node(value)
    # node.next = self.head
    # self.head = node
    self.head = Node(value, self.head)

  def includes(self, value):
    current = self.head
    while current:
      if current.value == value:
        return True
      else:
        current = current.next
    return False

  def __str__(self):
    current = self.head
    output = ""
    while current:
      output += "{ " + current.value + " } -> "
      current = current.next
    output += "NULL"

    return output



