arr0 = np.array([1, 2, 3])
expected_result =  arr0 / np.linalg.norm(arr0)
result = test(arr0)
assert np.array_equal(result, expected_result), 'Test failed'