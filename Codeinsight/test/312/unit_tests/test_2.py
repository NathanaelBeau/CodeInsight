# Test 3
mat0 = np.array([[-1, -2, -3], [-4, -5, -6]])
val0 = 0
expected_result =  6  # All values are negative, hence less than 0
result = test(mat0, val0)
assert result == expected_result, 'Test failed'