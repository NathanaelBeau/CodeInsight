var0 = 'banana'
var1 = 'col3'
lst0 = [{'col1': 1, 'col2': 'a', 'col3': 'apple'}, {'col1': 2, 'col2': 'b', 'col3': 'banana'}, {'col1': 3, 'col2': 'c', 'col3': 'cherry'}]
expected_result =  [{'col1': 2, 'col2': 'b', 'col3': 'banana'}]
result = test(var0, var1, lst0)
assert result==expected_result, 'Test failed'