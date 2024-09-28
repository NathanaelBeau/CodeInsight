var0 = pd.DataFrame({'B': [4, 5, 6]}, index=pd.Index([1, 2, 3], name='index_name'))
expected_result =  pd.DataFrame({'B': [4, 5, 6]}, index=pd.Index([1, 2, 3]))
result = test(var0)
assert result.equals(expected_result), 'Test failed'