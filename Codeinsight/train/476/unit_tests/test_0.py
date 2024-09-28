lst0 = ['Apple', 'apple', 'banana', 'BANANA', 'cherry']
expected_result =  ['apple', 'banana', 'cherry']
result = test(lst0)
assert result == expected_result, 'Test failed'