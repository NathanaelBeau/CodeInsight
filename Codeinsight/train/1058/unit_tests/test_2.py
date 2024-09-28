# Test 3
df0 = pd.DataFrame({'name': ['John', 'Jane', 'Doe', 'John', 'Jane']})
expected_result =  pd.DataFrame({'name': ['John', 'Jane', 'John', 'Jane']})
result = test(df0, 'name').reset_index(drop=True)
assert result.equals(expected_result), 'Test failed'