# Test 1
df0 = pd.DataFrame({'A': ['1-a', '2-b', '3-c']})
var0 = 'A'
var1 = 'B'
var2 = 'C'
var3 = '-'
expected_result =  pd.DataFrame({'A': ['1-a', '2-b', '3-c'], 'B': ['1', '2', '3'], 'C': ['a', 'b', 'c']})
result = test(df0, var0, var1, var2, var3)
assert result.equals(expected_result), 'Test failed'