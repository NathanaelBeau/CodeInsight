df0 = pd.DataFrame({'C': [7, 8, 9, 10]})
index_name0 = 'index_name'
expected_result =  pd.DataFrame({'C': [7, 8, 9, 10]}, index=pd.Index([0, 1, 2, 3], name='index_name'))
result = test(df0, index_name0)
assert result.equals(expected_result), 'Test failed'