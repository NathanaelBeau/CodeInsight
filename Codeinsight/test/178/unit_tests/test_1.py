dict2 = { 'e': 'world', 'f': None, 'g': [1, 2, 3], 'h': None }
expected_result2 = { 'e': 'updated', 'g': 'updated' }
assert test(dict2) == expected_result2, 'Test failed'