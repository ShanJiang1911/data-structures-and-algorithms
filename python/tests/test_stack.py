from stack_and_queue.stack import Stack
import pytest
from code_challenges.stack_and_queue.stack_and_queue.underflow_error import UnderflowError


def test_is_empty_when_empty():
  stack = Stack()
  actual = stack.is_empty()
  expected = True
  assert actual == expected


def test_psuh_empty():
  stack = Stack()
  stack.push("apple")
  actual = stack._top.value
  expected = "apple"
  assert actual == expected


def test_peek_empty():
  stack = Stack()
  with pytest.raises(UnderflowError):
    stack.peek()


def test_push_onto_full():
    s = Stack()
    s.push("apple")
    s.push("banana")
    s.push("cucumber")
    actual = s._top.value
    expected = "cucumber"
    assert actual == expected


def test_pop_single():
    s = Stack()
    s.push("apple")
    actual = s.pop()
    expected = "apple"
    assert actual == expected


def test_pop_some():
    s = Stack()

    s.push("apple")
    s.push("banana")
    s.push("cucumber")

    s.pop()

    actual = s.pop()
    expected = "banana"

    assert actual == expected


def test_check_not_empty():
    s = Stack()
    s.push("apple")
    s.push("banana")
    actual = s.is_empty()
    expected = False
    assert actual == expected

def test_pop_until_empty():
    s = Stack()
    s.push("apple")
    s.push("banana")
    s.push("cucumber")
    s.pop()
    s.pop()
    s.pop()
    actual = s.is_empty()
    expected = True
    assert actual == expected


def test_peek():
    s = Stack()
    s.push("apple")
    s.push("banana")
    actual = s.peek()
    expected = "banana"
    assert actual == expected


def test_pop_empty():
    s = Stack()
    with pytest.raises(UnderflowError) as e:
        s.pop()

    assert str(e.value) == "Method not allowed on empty collection"
