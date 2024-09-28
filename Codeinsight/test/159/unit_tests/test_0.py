# Test 1
df0 = pd.DataFrame(columns=['A', 'B'], dtype=int)
df1 = pd.DataFrame({'A': [1], 'B': [2]})
expected_result =  pd.DataFrame({'A': [1], 'B': [2]})
result = test(df0, df1)
assert result.equals(expected_result), 'Test failed'