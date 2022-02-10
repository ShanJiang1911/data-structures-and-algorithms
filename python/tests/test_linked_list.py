from linked_list.linked_list import Node, LinkedList


def test_create_Node():
    node = Node("apple")
    assert node.value == "apple"
    assert node.next == None

def test_node_next():
  apple = Node("apple")
  banana = Node("banana", apple)
  actual = banana.next
  expected = apple
  assert actual == expected

def test_linked_list():
  lst = LinkedList()
  assert lst.head is None

def test_insert_empty():
  lst = LinkedList()
  lst.insert("apple")
  assert lst.head.value == "apple"

def test_insert_not_empty():
  lst = LinkedList()
  lst.insert("apple")
  lst.insert("banana")
  assert lst.head.value == "banana"
  assert lst.head.next.value == "apple"

def test_includes_true():
  lst = LinkedList()
  lst.insert("apple")
  lst.insert("banana")
  actual = lst.includes("apple")
  expected = True
  assert actual == expected

def test_to_str():
  lst = LinkedList()
  lst.insert("apple")
  lst.insert("banana")
  assert str(lst) == "{ banana } -> { apple } -> NULL"
