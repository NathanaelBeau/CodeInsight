df0 = pd.DataFrame({'A': ['apple', 'banana', 'cherry'], 'B': ['old_value1', 'old_value2', 'grape']})
var0 = 'B'
lst0 = ['old_value1', 'old_value2']
var1 = 'new_value'
expected_result =  pd.DataFrame({'A': ['apple', 'banana', 'cherry'], 'B': ['new_value', 'new_value', 'grape']})
result = test(df0, var0, lst0, var1)
assert result.equals(expected_result), 'Test failed'