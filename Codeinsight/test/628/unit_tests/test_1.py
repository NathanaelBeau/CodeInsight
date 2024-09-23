lst0 = [{'value': 'baz'}, {'not_value': 'foo'}, {'value': 'qux'}]
expected_output = ['baz', 'qux']
assert test(lst0) ==expected_output, 'Test failed'