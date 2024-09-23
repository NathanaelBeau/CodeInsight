df0 = pd.DataFrame({ 'A': [1, 2, 3, 4, 5], 'B': ['a', 'b', 'c', 'd', 'e'], 'C': [10, 20, 30, 40, 50] })
var0 = 'C'
var1 = 40
var2 = 'B'
var3 = 'd'
expected_result =  pd.DataFrame({'A': [4], 'B': ['d'], 'C': [40]})
result = test(df0, var0, var1, var2, var3)
assert result.equals(expected_result), 'Test failed'