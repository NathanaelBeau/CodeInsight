# Test 2
ser0 = pd.Series(['a', 'b', 'c'])
expected_result =  np.array(['a', 'b', 'c'])
result = test(ser0)
assert np.array_equal(result, expected_result), 'Test failed'