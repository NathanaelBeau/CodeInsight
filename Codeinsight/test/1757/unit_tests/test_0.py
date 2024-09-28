lst0 = [
    {"name": "John", "age": 25},
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 22},
]
var0 = "name"
expected_output = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 22},
    {"name": "John", "age": 25},
]
assert test(lst0, var0) == expected_output, 'Test failed'