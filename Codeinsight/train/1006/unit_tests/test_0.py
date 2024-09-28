lst0 = [
    {'language': 'en', 'data': 'English Data'},
    {'language': 'fr', 'data': 'French Data'},
    {'language': 'es', 'data': 'Spanish Data'},
    {'language': 'en', 'data': 'Another English Data'}
]
var0 = 'language'
var1 = 'en'
expected_output = [
    {'language': 'en', 'data': 'English Data'},
    {'language': 'en', 'data': 'Another English Data'},
    {'language': 'fr', 'data': 'French Data'},
    {'language': 'es', 'data': 'Spanish Data'},
]
assert test(lst0, var0, var1) ==expected_output, 'Test failed'