# Test 3
df0 = pd.DataFrame({ 'animals': [['dog'], ['cat', 'dog'], ['cat']] })
col0 = 'animals'
expected_result =  pd.DataFrame({ 'cat': [0, 1, 1], 'dog': [1, 1, 0] })
result = test(df0, col0)
assert result.equals(expected_result), 'Test failed'