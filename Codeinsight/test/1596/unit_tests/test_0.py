df0 = pd.DataFrame({'cluster': [1, 2, 1, 2], 'value': [10, 20, 30, 40]})
col0 = 'cluster'
expected_result =  pd.DataFrame({'value': [20.0, 30.0]}, index=[1, 2])
assert test(df0, col0).equals(expected_result), 'Test failed'