lst0 = ['foo', 'bar', 'baz']
expected_output = {'foo': [1], 'bar': [], 'baz': []}
var0 = "foo"
var1 = 1
output = test(lst0, var0, var1)
assert output == expected_output, 'Test failed'