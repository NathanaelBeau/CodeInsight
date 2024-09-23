# Test 2
mat0 = np.array([[10, 20, 30], [40, 50, 60]])
val0 = 35
expected_result =  3  # 10 and 20 are less than 35
result = test(mat0, val0)
assert result == expected_result, 'Test failed'