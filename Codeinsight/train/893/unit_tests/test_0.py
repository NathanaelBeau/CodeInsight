df = pd.DataFrame({ 'col1': [1, 2, 3], 'col2': [4, 5, 6] })
expected_result =  pd.DataFrame({ 'col1': [3, 2, 1], 'col2': [6, 5, 4] })
result = test(df, 'col1', lambda x: -x)
assert result .equals( expected_result), 'Test failed'