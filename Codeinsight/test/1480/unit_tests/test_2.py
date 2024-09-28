df0 = pd.DataFrame({'M': [5, 6], 'N': [7, 8]})
lst0 = ['M']
expected_result =  np.array([[5], [6]])
result = test(df0, lst0)
assert np.array_equal(result, expected_result), 'Test failed'