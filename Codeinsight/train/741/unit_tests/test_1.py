df0 = pd.DataFrame({'A': ['one', 'two', 'three'], 'B': ['four', 'five', 'six']})
var0 = 'B'
expected_result =  pd.DataFrame({'A': ['one', 'two', 'three'], 'B': ['four', 'five', 'six']})
result = test(df0, var0)
assert result.equals(expected_result), 'Test failed'