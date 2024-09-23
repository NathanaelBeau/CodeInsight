dict0 = [
    {"key1": "value1", "key2": "value2"},
    {"key2": "value2", "key3": "value3"},
    {"key1": "value1", "key3": "value3"},
]
expected_output = {"key1", "key2", "key3"}
assert test(dict0) ==expected_output, 'Test failed'