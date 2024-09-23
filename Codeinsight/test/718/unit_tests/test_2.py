df0 = pd.DataFrame({ 'P': ['m', 'n', 'o'] }, index=[100, 200, 300])
expected_result =  pd.DataFrame({ 'P': ['m', 'n', 'o'] })
assert test(df0).equals(expected_result), 'Test failed'