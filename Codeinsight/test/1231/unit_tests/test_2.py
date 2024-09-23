arr0 = np.array([1.1, 2.2, 3.3])
expected_result =  np.array([1.1, 2.2, 3.3])
result = test(arr0)
assert np.array_equal(result, expected_result) and not np.may_share_memory(result, arr0), 'Test failed'