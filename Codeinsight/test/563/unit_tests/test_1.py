df0 = pd.DataFrame({'cluster': ['A', 'B', 'A', 'B'], 'value': [100, 200, 300, 400]})
col0 = 'cluster'
expected_result =  pd.DataFrame({'value': [200.0, 300.0]}, index=['A', 'B'])
assert test(df0, col0).equals(expected_result), 'Test failed'