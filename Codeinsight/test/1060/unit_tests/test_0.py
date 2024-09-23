df0 = pd.DataFrame({ 'A': [1, 2, 3], 'B': [4, 5, 6] })
expected_result =  pd.DataFrame({ 'A': [1, 10, 3], 'B': [4, 5, 6] })
result = test(df0, 'A', 2, 'A', 10)
assert result.equals(expected_result), 'Test failed'