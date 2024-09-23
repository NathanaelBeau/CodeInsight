df0 = pd.DataFrame({ 'P': ['m', 'n', 'o'], 'Q': [100, 200, 300] })
lst0 = [1]
expected_result =  pd.DataFrame({ 'P': ['m', 'o'], 'Q': [100, 300] }, index=[0, 2])
assert test(df0, lst0).equals(expected_result), 'Test failed'