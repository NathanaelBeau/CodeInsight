# Test 3
df0 = pd.DataFrame({'A': ['123', '456', '789'], 'B': ['ten', 'eleven', 'twelve']})
var0 = 'A'
var1 = r'^4'
expected_result =  pd.DataFrame({'A': ['456'], 'B': ['eleven']}, index=[1])
assert test(df0, var0, var1).equals(expected_result), 'Test failed'