df0 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
expected_output = [1, 4, 2, 5, 3, 6]
assert np.array_equal(test(df0) , (expected_output)), 'Test failed'