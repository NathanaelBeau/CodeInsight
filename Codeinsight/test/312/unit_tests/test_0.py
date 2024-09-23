# Test 1
mat0 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
val0 = 5
expected_result =  4  # 1, 2, 3, and 4 are less than 5
result = test(mat0, val0)
assert result == expected_result, 'Test failed'