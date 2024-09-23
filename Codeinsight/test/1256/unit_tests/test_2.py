df0 = pd.DataFrame({'G': ['apple', 'banana', 'cherry'], 'H': ['dog', 'cat', 'fish'], 'I': ['red', 'green', 'blue']})
var0 = 'banana'
expected_result3 = ['G']
result3 = test(df0, var0)
assert result3 == expected_result3, 'Test failed'