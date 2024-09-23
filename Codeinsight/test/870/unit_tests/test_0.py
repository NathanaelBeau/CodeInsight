lst0 = ['bar', 'baz']
var0 = "foo"
expected_result =  ['bar', 'baz', 'foo']
result = test(lst0, var0)
assert result == expected_result, 'Test failed'