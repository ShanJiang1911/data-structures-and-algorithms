from stack_and_queue.node import Node
from stack_and_queue.underflow_error import UnderflowError

class Stack:

  def __init__(self):
    self._top = None

  def is_empty(self):
    return self._top is None

  def peek(self):
    if self._top is None:
      raise UnderflowError("Method not allowed on empty collection")

    return self._top.value

  def push(self, value):
    self._top = Node(value, self._top)

  def pop(self):
    if self._top is None:
      raise UnderflowError("Method not allowed on empty collection")

    old_top = self._top

    self._top = self._top.next

    return old_top.value

    # old_top.next = None

    # old_value = old_top.value

    # old_top.value = None

    # return old_value

    # return old_top.value






