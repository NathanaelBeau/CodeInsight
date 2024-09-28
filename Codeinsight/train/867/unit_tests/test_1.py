dict0 = {'apple': 2, 'banana': 3, 'cherry': 1}
expected_result =  ['apple', 'apple', 'banana', 'banana', 'banana', 'cherry']
result = test(dict0)
assert result == expected_result, 'Test failed'