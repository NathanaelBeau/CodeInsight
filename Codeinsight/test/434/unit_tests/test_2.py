# Test 3
df0 = pd.DataFrame({'name': ['John', 'Jane', 'Doe', 'Smith', 'Roe']})
n = 1
expected_result =  pd.DataFrame({'name': ['Roe']})
result = test(df0, n).reset_index(drop=True)
assert result.equals(expected_result), 'Test failed'