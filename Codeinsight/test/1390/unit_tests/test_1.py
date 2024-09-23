df0 = pd.DataFrame({'X': ['a', 'b', 'c', 'a'], 'Y': ['e', 'f', 'g', 'h'], 'other_column': [50, 60, 70, 80]})
var0 = 'X'
var1 = 'a'
expected_result =  130
result = test(df0, var0, var1)
assert result == expected_result, 'Test failed'