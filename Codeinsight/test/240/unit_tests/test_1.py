arr0 = np.array([7, 8, 9], dtype=np.int64)
dtype0 = np.float64
expected_result =  np.array([7.0, 8.0, 9.0], dtype=np.float64)
result = test(arr0, dtype0)
assert np.array_equal(result, expected_result) and result.dtype == expected_result.dtype, 'Test failed'