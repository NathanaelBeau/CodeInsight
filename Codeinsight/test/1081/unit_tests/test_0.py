df0 = pd.DataFrame({ 'x': [None, 'HELLO', 'WORLD', None] })
expected_result =  pd.DataFrame({ 'x': [None, 'HELLO', 'WORLD', None] })
assert test(df0).equals(expected_result), 'Test failed'