from stack_and_queue.underflow_error import UnderflowError

class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

class Stack:

  def __init__(self):
    self._top = None

  def is_empty(self):
    return True

  def peek(self):
    if self._top is None:
      raise UnderflowError()
    return self._top.value

  def push(self, value):
    self._top = Node(value, self._top)

  def pop(self):
    if self._top is None:
      raise UnderflowError()
    old_top = self._top
    self._top = self._top.next
    return old_top.value




