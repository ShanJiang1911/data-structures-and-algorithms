from sorts.insertion_sort.insertion_sort.insertion_sort import insertion_sort

def test_insertion_sort():
  nums = [8, 4, 23, 42, 15, 12]
  insertion_sort(nums)
  expected = [4, 8, 12, 15, 23, 42]
  assert nums == expected
