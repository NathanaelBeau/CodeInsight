lst0 = [1, 2, [3, 4, [5, 6]], 7]
expected_result =  [1, 2, 3, 4, 5, 6, 7]
result = list(test(lst0))
assert result == expected_result, 'Test failed'