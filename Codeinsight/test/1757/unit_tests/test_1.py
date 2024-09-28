lst0 = [
    {"name": "Zoe", "age": 28},
    {"name": "Eva", "age": 35},
    {"name": "David", "age": 30},
]
var0 = "name"
expected_output = [
    {"name": "David", "age": 30},
    {"name": "Eva", "age": 35},
    {"name": "Zoe", "age": 28},
]
assert test(lst0, var0) == expected_output, 'Test failed'