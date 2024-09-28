lst0 = [1, 2, 3]
lst1 = [0, 0, 0]
lst2 = [-1, -2, -3]
expected_result =  [0, 0, 0]
result = test(lst0, lst1, lst2)
assert result == expected_result, 'Test failed'