lst0 = ['banana', 'apple', 'orange']
dict0 = [
    {'var0': 'apple', 'data': 'red'},
    {'var0': 'banana', 'data': 'yellow'},
    {'var0': 'orange', 'data': 'orange'}
]
var0 = 'var0'
expected_output = [
    {'var0': 'banana', 'data': 'yellow'},
    {'var0': 'apple', 'data': 'red'},
    {'var0': 'orange', 'data': 'orange'}
]
assert test(lst0, dict0, var0) ==expected_output, 'Test failed'