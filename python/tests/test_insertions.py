import pytest
from linked_list.linked_list import LinkedList

def test_append():
  lst = LinkedList["1", "2"]
  actual = lst.append["6"]
  expected = ["1", "2", "6"]
  assert actual == expected

def test_multiple_append():
  lst = LinkedList["1", "2"]
  actual = lst.append["6", "7", "8"]
  expected = ["1", "2", "6", "7", "8"]
  assert actual == expected


