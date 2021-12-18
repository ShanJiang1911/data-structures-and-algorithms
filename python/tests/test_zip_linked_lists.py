from code_challenges.zip_linked_lists import zip_linked_lists
from linked_list.linked_list import LinkedList

def test_zip_linked_lists():
  list_a = LinkedList() # add 1,2 and 3
  list_b = LinkedList() # add a,b and c

  actual = zip_linked_lists(list_a, list_b)
  expected = "whatever should be returned from function"

  assert actual == expected
