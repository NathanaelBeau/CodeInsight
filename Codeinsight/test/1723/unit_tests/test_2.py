# Test 3
df0 = pd.DataFrame({'M': [10, 11], 'N': [12, 13]})
var0 = 'split'
expected_result =  {'index': [0, 1], 'columns': ['M', 'N'], 'data': [[10, 12], [11, 13]]}
result = test(df0, var0)
assert result == expected_result, 'Test failed'