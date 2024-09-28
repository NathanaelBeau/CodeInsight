dict0 = {'apple': [10, 20, 30], 'banana': [5, 25, 50], 'cherry': [1, 2, 3]}
expected_result =  {'banana': [5, 25, 50], 'apple': [10, 20, 30], 'cherry': [1, 2, 3]}
result = test(dict0)
assert result == expected_result, 'Test failed'