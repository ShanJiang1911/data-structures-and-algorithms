from merge_sort import Mergesort

def test_merge_sort():
  arr = [8, 4, 23, 42, 16, 15]
  actual = Mergesort(arr)
  expected = [4, 8, 15, 16, 23, 42]
  assert actual == expected
