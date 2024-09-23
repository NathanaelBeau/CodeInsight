# Test 3
df0 = pd.DataFrame({'M': ['red', 'green', 'blue']})
column_name = 'M'
prefix_string = 'color_'
expected_result =  pd.DataFrame({'M': ['color_red', 'color_green', 'color_blue']})
result = test(df0, column_name, prefix_string)
assert result.equals(expected_result), 'Test failed'