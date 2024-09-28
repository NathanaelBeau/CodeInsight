# Test 2
df0 = pd.DataFrame({'X': [], 'Y': []})
df1 = pd.DataFrame({'X': ['apple'], 'Y': ['orange']})
expected_result =  pd.DataFrame({'X': ['apple'], 'Y': ['orange']})
result = test(df0, df1)
assert result.equals(expected_result), 'Test failed'