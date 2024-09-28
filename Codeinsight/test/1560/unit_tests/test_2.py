df0 = pd.DataFrame({'B': ['a', 'b', 'c', 'a', 'b']})
column_name0 = 'B'
expected_result =  [2, 2, 1]
result = test(df0, column_name0)
assert set(result) == set(expected_result), 'Test failed'