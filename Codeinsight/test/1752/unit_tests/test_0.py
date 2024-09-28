# Test with a list of integers
lst0 = [1, 2, 3, 4, 5, 6, 7, 8]
var0 = 2
expected_output = [[1, 2, 3, 4], [5, 6, 7, 8]]
assert test(lst0, var0) == expected_output, 'Test failed'