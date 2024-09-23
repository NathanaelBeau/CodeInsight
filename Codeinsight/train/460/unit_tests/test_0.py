# Unit Test 1
df0 = pd.DataFrame({ 'A': [1, 2, 3], 'B': [4, 5, 6] }, index=['x', 'y', 'z'])
expected_result =  pd.DataFrame({ 'A': [1, 2, 3], 'B': [4, 5, 6] })
result = test(df0)
assert result.equals(expected_result), 'Test failed'