df0 = pd.DataFrame({'E': ['blue', 'red', 'green'], 'F': ['old_value1', 'yellow', 'old_value2']})
var0 = 'F'
lst0 = ['old_value1', 'old_value2']
var1 = 'color'
expected_result =  pd.DataFrame({'E': ['blue', 'red', 'green'], 'F': ['color', 'yellow', 'color']})
result = test(df0, var0, lst0, var1)
assert result.equals(expected_result), 'Test failed'