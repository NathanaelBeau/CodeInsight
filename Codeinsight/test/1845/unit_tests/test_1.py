# Test 2
df0 = pd.DataFrame({'fruit': ['apple', 'banana', 'cherry', 'date', 'fig']})
n = 3
expected_result =  pd.DataFrame({'fruit': ['cherry', 'date', 'fig']})
result = test(df0, n).reset_index(drop=True)
assert result.equals(expected_result), 'Test failed'