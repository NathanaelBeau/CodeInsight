df0= pd.DataFrame({ 'a': [7, 8, 9], 'b': [2, 3, 1], 'c': [10, 11, 12] })
expected_result =  pd.DataFrame({ 'a': [9, 7, 8], 'b': [1, 2, 3], 'c': [12, 10, 11] }).reset_index(drop=True)
result = test(df0).reset_index(drop=True)
assert result.equals(expected_result), 'Test failed'