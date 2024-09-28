arr0 = np.array([4.5, 5.5, 6.5])
dtype0 = np.int32
expected_result =  np.array([4, 5, 6], dtype=np.int32)
result = test(arr0, dtype0)
assert np.array_equal(result, expected_result) and result.dtype == expected_result.dtype, 'Test failed'