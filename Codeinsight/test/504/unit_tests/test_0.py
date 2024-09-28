df0 = pd.DataFrame({ 'A': [1, 2, 3], 'B': [4, 5, 6], 'A_1': [7, 8, 9] })
expected_result =  pd.DataFrame({ 'A': [4, 5, 6], 'B': [4, 5, 6] })
assert test(df0).equals(expected_result), 'Test failed'