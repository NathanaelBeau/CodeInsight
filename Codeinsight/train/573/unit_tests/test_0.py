arr0 = np.array([1, 2, 3])
dtype0 = np.float32
expected_result =  np.array([1.0, 2.0, 3.0], dtype=np.float32)
result = test(arr0, dtype0)
assert np.array_equal(result, expected_result) and result.dtype == expected_result.dtype, 'Test failed'