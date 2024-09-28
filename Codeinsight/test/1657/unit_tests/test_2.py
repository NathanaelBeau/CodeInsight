dict0 = {'apple': (10, 8), 'banana': (6, 9), 'cherry': (2, 2)}
expected_result =  {'cherry': (2, 2), 'apple': (10, 8), 'banana': (6, 9)}
result = test(dict0)
assert result == expected_result, 'Test failed'