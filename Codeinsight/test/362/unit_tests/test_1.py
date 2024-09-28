df0 = pd.DataFrame({'key': ['A', 'B', 'A', 'C', 'B', 'A'], 'value': [1, 2, 3, 4, 5, 6]})
var0 = 'key'
var1 = 'B'
expected_result =  pd.DataFrame({'key': ['B', 'B'], 'value': [2, 5]})
result = test(df0, var0, var1)
assert (result.values == expected_result.values).all(), 'Test failed'