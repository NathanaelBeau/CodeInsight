df0 = pd.DataFrame({ 'A': [1, 2, 3, 4, 5], 'B': ['a', 'b', 'c', 'd', 'e'], 'C': [10, 20, 30, 40, 50] })
var0 = 'A'
var1 = 2
var2 = 'B'
var3 = 'b'
expected_result =  pd.DataFrame({'A': [2], 'B': ['b'], 'C': [20]})
result = test(df0, var0, var1, var2, var3)
assert result.equals(expected_result), 'Test failed'