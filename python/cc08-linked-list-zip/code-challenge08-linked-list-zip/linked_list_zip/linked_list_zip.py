class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


# Helper function to print list_a given linked list
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




def zip_linked_lists(list_a, list_b):

    current = Node()
    tail = current

    while True:
        if list_a is None:
            tail.next = list_b
            break

        elif list_b is None:
            tail.next = list_a
            break

    #     else:
    #         tail.next = list_a
    #         tail = list_a
    #         list_a = list_a.next

    #         tail.next = list_b
    #         tail = list_b
    #         list_b = list_b.next

    # return current.next
