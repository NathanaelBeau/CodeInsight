df0 = pd.DataFrame({'X': ['a', 'b', 'a', 'b'], 'Y': [10, 20, 30, 40]})
column_name0 = 'X'
expected_result =  pd.DataFrame({'X': ['a', 'b'], 'Y': [40, 60]})
result = test(df0, column_name0)
assert result.equals(expected_result), 'Test failed'