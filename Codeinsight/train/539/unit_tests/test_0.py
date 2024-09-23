lst0 = ["apple", "banana", "apple", "orange", "banana", "apple"]
expected_output = [('apple', 3), ('banana', 2), ('orange', 1)]
assert test(lst0) == expected_output, 'Test failed'