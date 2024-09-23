var0 = lambda x: len(x) == 3
lst0 = [[1, 2], [3, 4, 5], [5, 6, 7, 8]]
expected_result =  [[3, 4, 5]]
result = test(lst0, var0)
assert result == expected_result, 'Test failed'