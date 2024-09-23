df0 = pd.DataFrame({ 'A': [1, 2, 3, 4], 'B': ['a', 'b', 'a', 'b'], 'C': [10, 20, 30, 40] })
var0 = 'A'
var1 = 'B'
val0 = 1
val1 = 'a'
expected_result =  pd.DataFrame({ 'A': [1], 'B': ['a'], 'C': [10] })
result = test(df0, var0, var1, val0, val1)
assert result.equals(expected_result), 'Test failed'