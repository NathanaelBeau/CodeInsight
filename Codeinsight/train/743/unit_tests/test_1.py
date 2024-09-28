lst1 = [np.array([7]), np.array([8])]
expected_result =  np.array([[7], [8]])
result = test(lst1)
assert np.array_equal(result, expected_result), 'Test failed'