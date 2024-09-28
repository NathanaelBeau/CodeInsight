df0 = pd.DataFrame({'A': ['red', 'green', 'blue']})
var0 = r'e'
var1 = 'E'
expected_result =  pd.DataFrame({'A': ['rEd', 'grEEn', 'bluE']})
result = test(df0, 'A', var0, var1)
assert result.equals(expected_result), 'Test failed'