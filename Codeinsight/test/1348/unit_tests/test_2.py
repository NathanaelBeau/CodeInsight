lst0 = [[11, 12, 13, 14], [15, 16, 17, 18]]
expected_result =  [[0, 11, 0, 12, 0, 13, 0, 14], [0, 15, 0, 16, 0, 17, 0, 18]]
result = test(lst0)
assert result == expected_result, 'Test failed'