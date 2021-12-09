class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


# Helper function to print a given linked list
class LinkedList:

  def __init__(self):
    self.head = None

  def append(self, value):

    node = Node(value)

    if not self.head:
      self.head = node
      return

    current = self.head

    while current.next:
      current = current.next

    current.next = node




def zip_linked_lists(a, b):

    current = Node()
    tail = current

    while True:
        if a is None:
            tail.next = b
            break

        elif b is None:
            tail.next = a
            break

        else:
            tail.next = a
            tail = a
            a = a.next

            tail.next = b
            tail = b
            b = b.next

    return current.next
