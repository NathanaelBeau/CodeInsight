# Test 3
df0 = pd.DataFrame({'name': ['John', 'Jane', 'John', 'Jane'], 'age': [30, 25, 30, 26]})
lst0 = ['name']
expected_result =  pd.DataFrame({'name': ['John', 'Jane'], 'age': [30, 25]})
result = test(df0, lst0).reset_index(drop=True)
assert result.equals(expected_result), 'Test failed'