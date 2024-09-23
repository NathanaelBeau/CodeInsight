df0 = pd.DataFrame({ 'x': ['TEST', None, 'CASE', None] })
expected_result =  pd.DataFrame({ 'x': ['TEST', None, 'CASE', None] })
assert test(df0).equals(expected_result), 'Test failed'