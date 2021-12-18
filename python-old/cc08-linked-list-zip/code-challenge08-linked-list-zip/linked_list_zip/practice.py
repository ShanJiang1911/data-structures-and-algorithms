class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class LinkedList:
  def __init__(self):
    self.head = None

  def reverse(self):
    prev = None
    current = self.head
    while(current is not None):
      next = current.next
      current.next = prev
      prev = current
      current = next
    self.head = prev

  def push(self, newdata):
    new_node = Node(newdata)
    new_node.next = self.head
    self.head = new_node

  def print_list(self):
    value = self.head
    while(value):
      print(value.data)
      value = value.next

lst = LinkedList()
lst.push(5)
lst.push(15)
lst.push(25)

lst.print_list()
lst.reverse()
lst.print_list()
