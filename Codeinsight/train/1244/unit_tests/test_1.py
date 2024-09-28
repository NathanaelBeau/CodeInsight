# Test 2
df0 = pd.DataFrame({'X': ['apple/orange', 'banana/grape', 'cherry/peach']})
var0 = 'X'
var1 = 'Fruit1'
var2 = 'Fruit2'
var3 = '/'
expected_result =  pd.DataFrame({'X': ['apple/orange', 'banana/grape', 'cherry/peach'], 'Fruit1': ['apple', 'banana', 'cherry'], 'Fruit2': ['orange', 'grape', 'peach']})
result = test(df0, var0, var1, var2, var3)
assert result.equals(expected_result), 'Test failed'