lst0 = [[1], [2, 3], [4, 5, 6]]
length = 3
fill_value = 0
expected_output = [[1, 0, 0], [2, 3, 0], [4, 5, 6]]
assert test(lst0, length, fill_value) == expected_output, 'Test failed'