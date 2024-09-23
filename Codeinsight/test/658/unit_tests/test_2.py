df0 = pd.DataFrame({ 'Col1': [7.1, 8.2, 9.3], 'Col2': [10.4, 11.5, 12.6] })
expected_result =  pd.Series([7.1, 8.2, 9.3], name='Col1')
result = test(df0)
assert result.equals(expected_result), 'Test failed'