df0 = pd.DataFrame({'name': ['Alice', 'Bob', 'Charlie'], 'age': [25, 30, 35]})
var0 = 'name'
var1 = 'Bob'
expected_result =  1
result = test(df0, var0, var1)
assert result == expected_result, 'Test failed'