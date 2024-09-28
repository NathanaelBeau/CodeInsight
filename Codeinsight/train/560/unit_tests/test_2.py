var0 = 'col3'
var1 = [{'col1': 1, 'col2': 'a', 'col3': 'apple'}, {'col1': 2, 'col2': 'b', 'col3': 'banana'}]
expected_result =  ['apple', 'banana']
result = test(var0, var1)
assert result==expected_result, 'Test failed'