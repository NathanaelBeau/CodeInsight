df0 = pd.DataFrame({'C': ['m', 'n', 'm', 'o', 'n', 'p', 'm']})
column_name0 = 'C'
expected_result =  [3, 2, 1, 1]
result = test(df0, column_name0)
assert set(result) == set(expected_result), 'Test failed'