dict1 = { 'a': 1, 'b': None, 'c': 'hello', 'd': None }
expected_result1 = { 'a': 'updated', 'c': 'updated' }
assert test(dict1) == expected_result1, 'Test failed'