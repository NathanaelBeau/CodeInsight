var0 = lambda x: sum(x) < 10
lst0 = [[1, 2, 3], [3, 4, 5], [5, 6]]
expected_result =  [[1, 2, 3]]
result = test(lst0, var0)
assert result == expected_result, 'Test failed'