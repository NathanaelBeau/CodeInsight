var0 = 'B'
var1 = pd.DataFrame({'A': [1, 2, None, 4], 'B': [5, None, 7, 8], 'C': [9, 10, 11, None]})
var2 = 'C'
expected_result =  pd.DataFrame({'A': [1., 2., None, 4.], 'B': [5., 10., 7., 8.], 'C': [9., 10., 11., None]})
result = test(var0, var1, var2)
assert result.equals(expected_result), 'Test failed'