lst0 = [10, 20, 30, 40]
lst1 = ['X', 'Y']
expected_result =  [10, 'X', 20, 'Y']
result = test(lst0, lst1)
assert result == expected_result, 'Test failed'