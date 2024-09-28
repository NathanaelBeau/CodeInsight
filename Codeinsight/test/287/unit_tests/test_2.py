lst0 = [
    {"name": "Mary", "age": 29},
    {"name": "George", "age": 27},
    {"name": "Linda", "age": 33},
]
var0 = "name"
expected_output = [
    {"name": "George", "age": 27},
    {"name": "Linda", "age": 33},
    {"name": "Mary", "age": 29},
]
assert test(lst0, var0) == expected_output, 'Test failed'