df0 = pd.DataFrame({'c1': [3, 1, 2], 'c2': [1, 2, 3]})
col0 = 'c1'
col1 = 'c2'
expected_result =  pd.DataFrame({'c1': [1, 2, 3], 'c2': [2, 3, 1]}, index=[1, 2, 0])
assert test(df0, col0, col1).equals(expected_result), 'Test failed'