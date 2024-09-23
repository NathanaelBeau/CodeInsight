df0 = pd.DataFrame({ 'A': ['a', 'b', 'c'] }, index=[2, 5, 8])
expected_result =  pd.DataFrame({ 'A': ['a', 'b', 'c'] })
assert test(df0).equals(expected_result), 'Test failed'