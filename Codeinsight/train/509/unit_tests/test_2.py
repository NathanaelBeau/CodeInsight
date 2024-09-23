lst0 = [{'my_attr': True}, {'my_attr': False}, {'my_attr': True}]
var0 = 'my_attr'
expected_output = [True, False, True]
assert test(lst0, var0) ==expected_output, 'Test failed'