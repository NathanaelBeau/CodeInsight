df0 = pd.DataFrame({'C': ['apple', 'banana', 'cherry'], 'D': ['orange', 'old_value2', 'old_value1']})
var0 = 'D'
lst0 = ['old_value1', 'old_value2']
var1 = 'fruit'
expected_result =  pd.DataFrame({'C': ['apple', 'banana', 'cherry'], 'D': ['orange', 'fruit', 'fruit']})
result = test(df0, var0, lst0, var1)
assert result.equals(expected_result), 'Test failed'