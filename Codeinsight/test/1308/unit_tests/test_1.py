var0= pd.DataFrame({'A': [1, 2, 3, 2], 'B': [1, 1, 2, 3]})
expected_result =   pd.DataFrame({'A': [1, 2, 1], 'B': [2, 1, 1]}, index=[1, 2, 3])
result = test(var0)
assert result .equals( expected_result), 'Test failed'