df0 = pd.DataFrame({'A': ['cat', 'dog', 'fish']})
var0 = r'f'
var1 = 'F'
expected_result =  pd.DataFrame({'A': ['cat', 'dog', 'Fish']})
result = test(df0, 'A',var0, var1)
assert result.equals(expected_result), 'Test failed'