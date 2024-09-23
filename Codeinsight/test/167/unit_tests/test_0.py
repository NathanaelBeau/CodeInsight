df0 = pd.DataFrame({ 'a': [1, 2, 3], 'b': [3, 2, 1], 'c': [6, 5, 4] })
expected_result =  pd.DataFrame({ 'a': [3, 2, 1], 'b': [1, 2, 3], 'c': [4, 5, 6] }).reset_index(drop=True)
result = test(df0).reset_index(drop=True)
assert result.equals(expected_result), 'Test failed'