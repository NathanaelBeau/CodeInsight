df0 = pd.DataFrame({ 'A': [1, 2, 3], 'B': [4, 5, 6] })
lst0 = ['X', 'Y']
expected_result =  pd.DataFrame({ 'X': [1, 2, 3], 'Y': [4, 5, 6] })
assert test(df0.copy(), lst0).equals(expected_result), 'Test failed'