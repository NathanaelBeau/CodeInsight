# Test 1
df0 = pd.DataFrame({'A': ['appleX', 'bananaX', 'cherryX']})
column_name = 'A'
unwanted_string = 'X'
expected_result =  pd.DataFrame({'A': ['apple', 'banana', 'cherry']})
result = test(df0, column_name, unwanted_string)
assert result.equals(expected_result), 'Test failed'