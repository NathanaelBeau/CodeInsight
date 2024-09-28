# Test 3
df0 = pd.DataFrame({ 'X': ['apple', 'banana', 'cherry'], 'Y': ['dog', 'elephant', 'fox'] })
var0 = 'X'
expected_result =  'apple'
result = test(df0, var0)
assert result == expected_result, 'Test failed'