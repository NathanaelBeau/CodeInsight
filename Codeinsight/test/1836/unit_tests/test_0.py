lst0 = [1, 2, 3, 4, 5]
lst1 = [4, 5, 6]
n = 3
expected_result =  [1, 2, 3]
result = test(lst0, lst1, n)
assert result == expected_result, 'Test failed'