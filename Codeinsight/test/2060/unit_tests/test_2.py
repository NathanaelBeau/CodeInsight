lst0 = ['foo', 'bar', 'baz']
expected_output = {'foo': [1], 'bar': [], 'baz': []}
var0 = "foo"
output = test(lst0, var0)
assert output == expected_output, 'Test failed'