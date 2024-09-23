var0 = 'A'
var1 = pd.DataFrame({'A': [1, 2, None, 4], 'B': [5, None, 7, 8], 'C': [9, 10, 11, None]})
var2 = 'B'
expected_result =  pd.DataFrame({'A': [1.0, 2.0, 7.0, 4.0], 'B': [5.0, None, 7.0, 8.0], 'C': [9.0, 10.0, 11.0, None]})
result = test(var0, var1, var2)
assert result.equals(expected_result), 'Test failed'