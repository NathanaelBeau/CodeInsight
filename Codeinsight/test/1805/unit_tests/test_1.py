dict0 = {1: 'one', 2: 'two', 3: 'three'}
expected_result =  {'one': 1, 'two': 2, 'three': 3}
result = test(dict0)
assert result == expected_result, 'Test failed'