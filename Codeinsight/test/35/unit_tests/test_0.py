df1 = pd.DataFrame({'A': [1, 2, None, 4], 'B': [5., 6., 7., 8.]})
expected_result =  pd.DataFrame({'A': [1., 2., 7., 4.], 'B': [5., 6., 7., 8.]})
result = test(df1, 'A', 'B')
assert result .equals( expected_result), 'Test failed'