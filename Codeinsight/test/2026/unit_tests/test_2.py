df0 = pd.DataFrame({ 'E': [11, 12, 13, 14], 'F': [15, 16, 17, 18] }, index=['r', 's', 't', 'u'])
expected_result =  pd.DataFrame({ 'index': ['r', 's', 't', 'u'], 'E': [11, 12, 13, 14], 'F': [15, 16, 17, 18] })
result = test(df0)
assert result.equals(expected_result), 'Test failed'