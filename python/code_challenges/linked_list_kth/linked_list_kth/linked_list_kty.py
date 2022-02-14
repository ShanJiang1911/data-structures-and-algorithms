from asyncio.windows_events import NULL
from pyparsing import null_debug_action


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


  def get_kth_from_end(self, k):

    def reverse(self):
      current = self.head
      prev = NULL
      while current:
        next = current.next
        current.next = prev
        prev = current
        current = next
      return current

    reverse(self)

    def show(self):
      lst = []
      current = self.head
      while current:
        lst.append(current.value)
        current = current.next
      return lst

    



