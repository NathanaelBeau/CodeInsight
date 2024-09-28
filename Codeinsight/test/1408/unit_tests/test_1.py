# Test 3
df0 = pd.DataFrame({'D': [2, 4], 'E': [6, 8], 'F': [10, 12]})
var0 = '^D|F$'
var1 = 2
expected_result =  pd.DataFrame({'D': [1.0, 2.0], 'E': [6, 8], 'F': [5.0, 6.0]})
assert test(df0, var0, var1).equals(expected_result), 'Test failed'