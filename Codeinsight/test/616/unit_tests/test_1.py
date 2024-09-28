df0 = pd.DataFrame({'A': ['apple', 'banana', 'cherry', 'date'], 'B': ['grape', 'honeydew', 'kiwi', 'lemon']})
var0 = 'A'
lst0 = ['apple', 'banana']
expected_result =  pd.DataFrame({'A': ['apple', 'banana'], 'B': ['grape', 'honeydew']})
result = test(df0, var0, lst0)
assert result.equals(expected_result), 'Test failed'