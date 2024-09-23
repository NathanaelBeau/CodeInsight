arr0 = np.array([[1, 2], [3, 4], [5, 6]])
expected_result =  arr0
result = test(arr0)
assert np.array_equal(result, expected_result), 'Test failed'