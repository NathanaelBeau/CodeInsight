df0 = pd.DataFrame({'B': [4, 5, 6]})
index_name0 = 'my_index'
expected_result =  pd.DataFrame({'B': [4, 5, 6]}, index=pd.Index([0, 1, 2], name='my_index'))
result = test(df0, index_name0)
assert result.equals(expected_result), 'Test failed'