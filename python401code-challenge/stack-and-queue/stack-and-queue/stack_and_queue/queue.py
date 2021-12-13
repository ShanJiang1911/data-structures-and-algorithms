from stack_and_queue.underflow_error import UnderflowError
from stack_and_queue.node import Node


class Queue:

  def __init__(self):
    self._front = None
    self._rear = None

  def is_empty(self):
    return self._rear is None

  def peek(self):
    if self._front is None:
        raise UnderflowError()

    return self._front.value

  def enqueue(self, value):

    self._rear = Node(value, self._rear)

    if self._front is None:
      self._front = self._rear

  def dequeue(self):
    if self._front is None:
      raise UnderflowError()

    old_front = self._front

    self._front = self._front.next

    old_front.next = None

    return old_front.value

