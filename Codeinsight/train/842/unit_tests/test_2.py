var0 = 'C'
var1 = 0.5
df0 = pd.DataFrame({'A': [13, 14, 15], 'B': [16, 17, 18], 'C': [19, 20, 21]})
expected_result =  pd.DataFrame({'A': [13, 14, 15], 'B': [16, 17, 18], 'C': [9.5, 10.0, 10.5]})
result = test(df0.copy(), var0, var1)
assert result.equals(expected_result), 'Test failed'