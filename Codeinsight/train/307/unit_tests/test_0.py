# Test 1
df0 = pd.DataFrame({ 'fruits': [['apple', 'banana'], ['apple'], ['banana', 'cherry']] })
col0 = 'fruits'
expected_result =  pd.DataFrame({ 'apple': [1, 1, 0], 'banana': [1, 0, 1], 'cherry': [0, 0, 1] })
result = test(df0, col0)
assert result.equals(expected_result), 'Test failed'