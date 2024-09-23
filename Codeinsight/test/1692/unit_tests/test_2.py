df0 = pd.DataFrame({'E': [12, 13, 14], 'F': [15, 16, 17]})
expected_result =  pd.DataFrame({'E': [12, 13, 14], 'F': [15, 16, 17]})
result = test(df0)
assert result.equals(expected_result), 'Test failed'