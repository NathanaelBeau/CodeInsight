df0= pd.DataFrame({ 'a': [4, 5, 6], 'b': [1, 1, 1], 'c': [7, 8, 9] })
expected_result =  pd.DataFrame({ 'a': [6, 5, 4], 'b': [1, 1, 1], 'c': [9, 8, 7] }).reset_index(drop=True)
result = test(df0).reset_index(drop=True)
assert result.equals(expected_result), 'Test failed'