arr0 = np.array([[0,1],[1,0],[0,1],[1,1]])
expected_result =  ([0, 2])
result = test(arr0)
assert np.array_equal(result, expected_result), 'Test failed'