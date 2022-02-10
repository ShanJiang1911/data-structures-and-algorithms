from stack_and_queue.queue import Queue
from code_challenges.stack_and_queue.stack_and_queue.underflow_error import UnderflowError
import pytest



def test_is_empty_when_empty():
  queue = Queue()
  actual = queue.is_empty()
  expected = True
  assert actual == expected

def test_peek_empty():
  queue = Queue()
  with pytest.raises(UnderflowError):
    queue.peek()

def test_enqueue():
    queue = Queue()
    queue.enqueue("apple")
    queue.enqueue("banana")
    actual = queue.peek()
    expected = "apple"
    assert actual == expected


def test_dequeue():
    q = Queue()
    q.enqueue("apple")
    q.enqueue("banana")
    actual = q.dequeue()
    expected = "apple"
    assert actual == expected


def test_peek():
    q = Queue()
    q.enqueue("apple")
    q.enqueue("banana")
    q.enqueue("cucumber")
    actual = q.peek()
    expected = "apple"
    assert actual == expected

def test_enqueue_one():
    q = Queue()
    q.enqueue("apples")
    actual = q.peek()
    expected = "apples"
    assert actual == expected


def test_enqueue_two():
    q = Queue()
    q.enqueue("apples")
    q.enqueue("bananas")
    actual = q.peek()
    expected = "apples"
    assert actual == expected


def test_dequeue_when_empty():
    q = Queue()
    with pytest.raises(UnderflowError):
        q.dequeue()


def test_dequeue_when_full():
    q = Queue()
    q.enqueue("apples")
    q.enqueue("bananas")
    actual = q.dequeue()
    expected = "apples"
    assert actual == expected


def test_peek_post_dequeue():
    q = Queue()
    q.enqueue("apples")
    q.enqueue("bananas")
    q.dequeue()
    actual = q.peek()
    expected = "bananas"
    assert actual == expected

def test_exhausted():
    q = Queue()
    q.enqueue("apple")
    q.enqueue("banana")
    q.enqueue("cucumber")
    q.dequeue()
    q.dequeue()
    q.dequeue()
    actual = q.is_empty()
    expected = True
    assert actual == expected



