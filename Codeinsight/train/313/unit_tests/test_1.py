lst0 = ['apple', 'banana', 'cherry']
lst1 = ['apple', 'pear']
expected_result =  ['banana', 'cherry']
result = test(lst0, lst1)
assert result == expected_result, 'Test failed'