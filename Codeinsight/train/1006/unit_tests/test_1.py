lst0_3 = [
    {'language': 'es', 'data': 'Spanish Data'},
    {'language': 'fr', 'data': 'French Data'},
    {'language': 'en', 'data': 'English Data'}
]
var0_3 = 'language'
var1_3 = 'fr'
expected_output_3 = [
    {'language': 'fr', 'data': 'French Data'},
    {'language': 'es', 'data': 'Spanish Data'},
    {'language': 'en', 'data': 'English Data'}
]
assert test(lst0_3, var0_3, var1_3) == expected_output_3, 'Test failed'