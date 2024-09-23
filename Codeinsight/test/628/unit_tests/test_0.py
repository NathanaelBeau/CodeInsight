lst0 = [{'value': 'foo'}, {'value': 'bar'}, {'not_value': 'baz'}]
expected_output = ['foo', 'bar']
assert test(lst0) ==expected_output, 'Test failed'