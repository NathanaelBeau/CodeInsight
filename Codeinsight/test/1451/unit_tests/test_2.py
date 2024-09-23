# Test 3
df0 = pd.DataFrame({'words': ['sunny day', 'rainy night', 'cloudy morning']})
column_name = 'words'
lst0 = ['sunny', 'cloudy']
expected_result =  pd.Series([True, False, True])
result = test(df0, column_name, lst0)
assert result.equals(expected_result), 'Test failed'