lst0 = ['b', 'c', 'a']
dict0 = [
    {'var0': 'a', 'data': 1},
    {'var0': 'b', 'data': 2},
    {'var0': 'c', 'data': 3}
]
var0 = 'var0'
expected_output = [
    {'var0': 'b', 'data': 2},
    {'var0': 'c', 'data': 3},
    {'var0': 'a', 'data': 1}
]
assert test(lst0, dict0, var0) ==expected_output, 'Test failed'