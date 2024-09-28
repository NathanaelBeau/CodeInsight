lst0 = [
    {'link': 'http://example.com/1/', 'id': 1},
    {'link': 'http://example.com/2/', 'id': 2},
    {'link': 'http://example.com/3/', 'id': 3},
]
var0 = 'id'
lst1 = [4, 5]
expected_output = lst0
assert test(lst0, var0, lst1) == expected_output, 'Test failed'