var0 = pd.DataFrame({'A': ['apple', 'banana', 'apple'], 'B': ['orange', 'orange', 'apple']})
expected_result =  pd.DataFrame({'A': [2., 1., 0.], 'B': [1., 0., 2.]}, index=['apple', 'banana', 'orange'])
result = test(var0)
assert result .equals( expected_result), 'Test failed'