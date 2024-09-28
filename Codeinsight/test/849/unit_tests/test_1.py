df0 = pd.DataFrame({ 'X': ['apple', 'banana', 'cherry'], 'Y': ['dog', 'cat', 'mouse'] })
expected_result =  pd.Series(['apple', 'banana', 'cherry'], name='X')
result = test(df0)
assert result.equals(expected_result), 'Test failed'