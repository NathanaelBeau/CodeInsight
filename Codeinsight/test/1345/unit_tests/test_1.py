var0 = 'apple'
var1 = 'fruits'
var2 = 'banana'
df0 = pd.DataFrame({'fruits': ['apple', 'orange'], 'count': [10, 15]})
expected_result =  pd.DataFrame({'fruits': ['banana', 'orange'], 'count': [10, 15]})
result = test(df0, var0, var1, var2)
assert result.equals(expected_result), 'Test failed'