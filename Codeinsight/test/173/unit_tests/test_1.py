lst0 = [{'my_attr': 123}, {'my_attr': 456}, {'my_attr': 789}]
var0 = 'my_attr'
expected_output = [123, 456, 789]
assert test(lst0, var0) ==expected_output, 'Test failed'