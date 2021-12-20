class Node:
  def __init__(self, dataval = None):
    self.dataval = dataval
    self.nextval = None



class LinkedList:

  def __init__(self, headval = None):
    self.headval = headval

  def append(self, newNode):
    if self.headval == None:
      self.headval = newNode
    else:
      currentNode = self.headval
      while currentNode != None:
        if currentNode.nextval == None:
          currentNode.nextval = newNode
          break
        else:
          currentNode = currentNode.nextval

  def add_before(self, targetVal, newNode):
    currentNode = self.headval
    previousNode = None
    while currentNode != None:
      if currentNode.val == targetVal:
        newNode.nextval = currentNode
        if previousNode == None:
          self.headval = newNode
        else:
          previousNode.nextval = newNode
          return 0


