lst0 = ['apple', 'banana', 'cherry']
lst1 = [3, 2, 1]
expected_result =  {'apple': 3, 'banana': 2, 'cherry': 1}
result = test(lst0, lst1)
assert result == expected_result, 'Test failed'