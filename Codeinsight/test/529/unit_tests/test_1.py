df1 = pd.DataFrame({'B': ['a', 'a', 'b', 'c', 'c', 'c']})
col1 = 'B'
expected_result =  pd.DataFrame({'B': ['a', 'a', 'b', 'c', 'c', 'c'], 'compared': [False, True, False, False, True, True]})
result = test(df1, col1)
assert result.equals(expected_result), 'Test failed'