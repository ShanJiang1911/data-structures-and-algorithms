from .hashmap_repeated_word import RepeatedWord

def test_repeated_word():
  string = "Once upon a time, finds the first word to occur more than Once in a string"
  actual = RepeatedWord(string)
  expected = "Once"
  assert actual == expected
