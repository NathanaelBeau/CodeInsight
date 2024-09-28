df0 = pd.DataFrame({'A': [1, 2, 3]})
index_name0 = 'new_index'
expected_result =  pd.DataFrame({'A': [1, 2, 3]}, index=pd.Index([0, 1, 2], name='new_index'))
result = test(df0, index_name0)
assert result.equals(expected_result), 'Test failed'