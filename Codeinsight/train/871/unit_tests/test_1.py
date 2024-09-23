lst0 = ['apple', 'banana', 'cherry']
lst1 = [False, True, False]
expected_result =  ['banana']
result = test(lst0, lst1)
assert result == expected_result, 'Test failed'