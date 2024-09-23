df0 = pd.DataFrame({'cluster': [3, 3, 3], 'value': [1, 2, 3]})
col0 = 'cluster'
expected_result =  pd.DataFrame({'value': [2.0]}, index=[3])
assert test(df0, col0).equals(expected_result), 'Test failed'