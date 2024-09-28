lst0 = [2, 3, 7]
lst1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
expected_result =  [1, 4, 5, 6, 8, 9]
result = test(lst0, lst1)
assert result == expected_result, 'Test failed'