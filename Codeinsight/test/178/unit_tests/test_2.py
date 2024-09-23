dict3 = { 'i': {'key': 'value'}, 'j': None, 'k': (1, 2), 'l': None }
expected_result3 = { 'i': 'updated', 'k': 'updated' }
assert test(dict3) == expected_result3, 'Test failed'