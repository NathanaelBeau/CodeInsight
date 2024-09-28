var0 = 'col2'
var1 = [{'col1': 'x', 'col2': 'a'}, {'col1': 'y', 'col2': 'b'}, {'col1': 'z', 'col2': 'c'}]
expected_result =  ['a', 'b', 'c']
result = test(var0, var1)
assert result==expected_result, 'Test failed'