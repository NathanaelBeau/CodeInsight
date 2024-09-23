lst0 = ["Hello\tWorld", "Python\tis\tfun"]
expected_output = [["Hello", "World"], ["Python", "is", "fun"]]
assert test(lst0) == expected_output, 'Test failed'