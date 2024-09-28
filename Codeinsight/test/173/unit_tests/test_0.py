lst0 = [{'my_attr': 'value1'}, {'my_attr': 'value2'}, {'my_attr': 'value3'}]
var0 = 'my_attr'
expected_output = ['value1', 'value2', 'value3']
assert test(lst0, var0) ==expected_output, 'Test failed'