lst0 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
var0 = 4
expected_output = [[1, 2, 3, 4], [5, 6, 7, 8], [9]]
result = list(test(lst0, var0))
assert result == expected_output, 'Test failed'