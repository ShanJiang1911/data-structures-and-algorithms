class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

class LinkedList:
  def __init__(self):
    self.head = None

  def append(self, value):

    node = Node(value)

    if not self.head:
      self.head = node
      return

    current = self.head

    while current:
      if current.next is None:
        current.next = Node(value)
        break
    current = current.next


  def get_kth_from_end(head, k):

    n = 0
    current = head

