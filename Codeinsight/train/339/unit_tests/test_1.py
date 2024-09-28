# Test 2
df0 = pd.DataFrame({'B': ['helloY', 'worldY', 'testY']})
column_name = 'B'
unwanted_string = 'Y'
expected_result =  pd.DataFrame({'B': ['hello', 'world', 'test']})
result = test(df0, column_name, unwanted_string)
assert result.equals(expected_result), 'Test failed'