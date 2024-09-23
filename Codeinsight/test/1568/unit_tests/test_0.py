df0 = pd.DataFrame({'A': [1, 2, 3]}, index=pd.Index([4, 5, 6], name='index_name'))
expected_result =  pd.DataFrame({'A': [1, 2, 3]}, index=pd.Index([4, 5, 6]))
result = test(df0)
assert result.equals(expected_result), 'Test failed'