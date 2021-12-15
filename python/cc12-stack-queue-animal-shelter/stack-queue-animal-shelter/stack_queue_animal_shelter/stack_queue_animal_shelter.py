class Node:
    def __init__(self, value, next_=None):
        self.value = value
        self.next = next_

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, value):
        node = Node(value)
        if self.rear:
            self.rear.next = node
        self.rear = node
        self.front = self.front or self.rear

    def dequeue(self):
        if not self.front:
            raise InvalidOperationError("Empty")
        temp = self.front
        self.front = self.front.next
        temp.next = None
        return temp.value

    def peek(self):
        if not self.front:
            raise InvalidOperationError("Empty")
        return self.front.value

    def is_empty(self):
        return self.front is None

class InvalidOperationError(Exception):
    pass



class Dog:
  pass

class Cat:
  pass

class AnimalShelter(Dog, Cat):
  pass

  def dog_cat():

    dog_found = False

    return dog_found

