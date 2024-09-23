dict0 = { 'age': {'context': 2}, 'address': {'context': 4}, 'name': {'context': 1} }
var0 = 'context'
expected_output = { 'name': {'context': 1}, 'age': {'context': 2}, 'address': {'context': 4} }
assert test(dict0, var0) ==expected_output, 'Test failed'