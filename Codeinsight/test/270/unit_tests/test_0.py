lst0 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
var0= 3
expected_output = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10]]
result = list(test(lst0, var0))
assert result == expected_output, 'Test failed'