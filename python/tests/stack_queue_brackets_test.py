from code_challenges.stack_queue_brackets.stack_queue_brackets.stack_queue_brackets import Check

def test_valid():
  string = "{[]{()}}"
  actual = Check.check_match(string)
  expected = True
  assert actual == expected


def test_valid2():
  string = "([{()]}"
  actual = Check.check_match(string)
  expected = False
  assert actual == expected

