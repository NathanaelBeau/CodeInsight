df0 = pd.DataFrame({ 'C': [7, 8], 'D': [9, 10] }, index=['p', 'q'])
expected_result =  pd.DataFrame({ 'index': ['p', 'q'], 'C': [7, 8], 'D': [9, 10] })
result = test(df0)
assert result.equals(expected_result), 'Test failed'