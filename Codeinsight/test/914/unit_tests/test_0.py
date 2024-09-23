var0 = lambda x: all(i > 2 for i in x)
lst0 = [[1, 2, 3], [3, 4, 5], [5, 6, 7]]
expected_result =  [[3, 4, 5], [5, 6, 7]]
result = test(lst0, var0)
assert result == expected_result, 'Test failed'