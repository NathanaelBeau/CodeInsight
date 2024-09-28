# Test 3
df0 = pd.DataFrame({'M': [1.5, 2.5], 'N': [3.5, 4.5]})
expected_result =  np.array([(1.5, 3.5), (2.5, 4.5)])
result = test(df0)
assert np.array_equal(result, expected_result), 'Test failed'