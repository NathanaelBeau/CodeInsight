lst0 = ['id3', 'id1', 'id2']
dict0 = [
    {'var0': 'id1', 'data': 'A'},
    {'var0': 'id2', 'data': 'B'},
    {'var0': 'id3', 'data': 'C'}
]
var0 = 'var0'
expected_output = [
    {'var0': 'id3', 'data': 'C'},
    {'var0': 'id1', 'data': 'A'},
    {'var0': 'id2', 'data': 'B'}
]
assert test(lst0, dict0, var0) ==expected_output, 'Test failed'