class Node:
  def __init__(self, value):
    self.value = value

class KaryTree:
  def __init__(self, root=None):
    self.root = root



def fizz_buzz_tree(tree):
  KaryTreeList = []
  newKaryTreeList = []

<<<<<<< HEAD
  # for i in KaryTreeList:
  #   if i.value%3 == 0:
  #     i = "Fizz"
  #   elif i.value%5 == 0:
  #     i = "Buzz"
  #   elif i.value%3 == 0 and i.value%5 == 0:
  #     i = "FizzBuzz"
  #   else:
  #     i = str(i)
  #   newKaryTreeList.append(i)
  # return newKaryTreeList
=======
  for i in KaryTreeList:
    if i.value%3 == 0:
      i = "Fizz"
    elif i.value%5 == 0:
      i = "Buzz"
    elif i.value%3 == 0 and i.value%5 == 0:
      i = "FizzBuzz"
    else:
      i = str(i)
    newKaryTreeList.append(i)
  return newKaryTreeList
>>>>>>> b1be8ca99b92aec244412aafe6d34071cb3efad2



