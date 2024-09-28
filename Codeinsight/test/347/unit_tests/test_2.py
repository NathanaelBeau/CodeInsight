# Test 3
df0 = pd.DataFrame({ 'Score': [90, 85, 85, 95] }, index=[1, 2, 2, 3])
expected_result =  pd.DataFrame({ 'Score': [90, 85, 95] }, index=[1, 2, 3])
result = test(df0)
assert result.equals(expected_result), 'Test failed'