lst0 = ['hello', 1, 'world', 2, '!', 3]
expected_result =  {'hello': 1, 'world': 2, '!': 3}
result = test(lst0)
assert result == expected_result, 'Test failed'