var0 = 2
var1 = 'col1'
lst0 = [{'col1': 1, 'col2': 'a'}, {'col1': 2, 'col2': 'b'}, {'col1': 3, 'col2': 'c'}]
expected_result =  [{'col1': 2, 'col2': 'b'}]
result = test(var0, var1, lst0)
assert result==expected_result, 'Test failed'