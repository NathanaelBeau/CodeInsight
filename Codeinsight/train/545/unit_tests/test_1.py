dict0 = {0: {'name_first': 'John', 'name_last': 'Doe'}}
var0 = {'name_first': 'Jane', 'name_last': 'Smith'}
expected_output = {0: {'name_first': 'John', 'name_last': 'Doe'}, 1: {'name_first': 'Jane', 'name_last': 'Smith'}}
assert test(dict0, var0) == expected_output, 'Test failed'