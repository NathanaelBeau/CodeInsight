df0 = pd.DataFrame({ 'x': [None, None, None, 'FOO'] })
expected_result =  pd.DataFrame({ 'x': [None, None, None, 'FOO'] })
assert test(df0).equals(expected_result), 'Test failed'