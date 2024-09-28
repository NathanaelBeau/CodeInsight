var0 = 'col1'
var1 = [{'col1': 1, 'col2': 'a'}, {'col1': 2, 'col2': 'b'}, {'col1': 3, 'col2': 'c'}]
expected_result =  [1, 2, 3]
result = test(var0, var1)
assert result==expected_result, 'Test failed'