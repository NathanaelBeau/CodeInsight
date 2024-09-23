df0 = pd.DataFrame({'A': ['x', 'y', 'x', 'z', 'y', 'x']})
column_name0 = 'A'
expected_result =  [3, 2, 1]
result = test(df0, column_name0)
assert set(result) == set(expected_result), 'Test failed'