# Test 3
ser0 = pd.Series([7, 8, 9], name='Alpha')
ser1 = pd.Series([10, 11, 12], name='Beta')
expected_result =  pd.DataFrame({'Alpha': [7, 8, 9], 'Beta': [10, 11, 12]})
result = test(ser0, ser1)
assert result.equals(expected_result), 'Test failed'