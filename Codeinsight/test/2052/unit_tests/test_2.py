df0 = pd.DataFrame({ 'A': [1, 2, 3, 4], 'B': ['a', 'b', 'a', 'b'], 'C': [10, 20, 30, 40] })
var0 = 'B'
var1 = 'C'
val0 = 'b'
val1 = 40
expected_result =  pd.DataFrame({ 'A': [4], 'B': ['b'], 'C': [40] }).reset_index(drop=True)
result = test(df0, var0, var1, val0, val1).reset_index(drop=True)
assert result.equals(expected_result), 'Test failed'