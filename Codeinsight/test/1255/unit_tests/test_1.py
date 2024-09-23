dict0 = { 'age': {'context': 2}, 'address': {'context': 2}, 'name': {'context': 2} }
var0 = 'context'
expected_output = { 'age': {'context': 2}, 'address': {'context': 2}, 'name': {'context': 2} }
assert test(dict0, var0) ==expected_output, 'Test failed'