dict0 = {'name': 'John', 'age': 30, 'gender': 'Male'}
var0 = 'name'
var1 = 'city'
var2 = 'gender'
expected_output = {'name': 'John', 'city': None, 'gender': 'Male'}
assert test(dict0, var0, var1, var2) ==expected_output, 'Test failed'