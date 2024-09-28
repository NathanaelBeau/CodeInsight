lst0_4 = [
    {'language': 'en', 'data': 'English Data'},
    {'language': 'en', 'data': 'Another English Data'}
]
var0_4 = 'language'
var1_4 = 'fr'
expected_output_4 = [
    {'language': 'en', 'data': 'English Data'},
    {'language': 'en', 'data': 'Another English Data'}
]
assert test(lst0_4, var0_4, var1_4) == expected_output_4, 'Test failed'