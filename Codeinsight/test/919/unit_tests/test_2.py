df0 = pd.DataFrame({'M': [11, 12, 13], 'N': [14, 15, 16]})
expected_result =  0
result = test(df0)
assert result == expected_result, 'Test failed'