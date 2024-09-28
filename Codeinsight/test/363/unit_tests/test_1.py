df0 = pd.DataFrame({'A': [10, 20, 30, 40, 50], 'B': [50, 60, 70, 80, 90]})
var0 = 'A'
var1 = 30
var2 = 'B'
expected_result =  pd.DataFrame({'A': [10, 20, 30, 40, 50], 'B': [50, 60, 30, 80, 90]})
result = test(df0, var0, var1, var2)
assert result.equals(expected_result), 'Test failed'