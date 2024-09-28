df0 = pd.DataFrame({ 'X': ['w', 'x', 'y'] }, index=[10, 20, 30])
expected_result =  pd.DataFrame({ 'X': ['w', 'x', 'y'] })
assert test(df0).equals(expected_result), 'Test failed'