lst0 = [[1, 2, 3.5], [4, 5, 1.2], [6, 7, 2.8]]
expected_result =  [[4, 5, 1.2], [6, 7, 2.8], [1, 2, 3.5]]
result = test(lst0)
assert result == expected_result, 'Test failed'