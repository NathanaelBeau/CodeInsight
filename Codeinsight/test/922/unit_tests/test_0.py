dictA = {"a": "duck duck goose", "b": "duck goose", "c": "duck duck duck"}
str0 ="duck"
expected_output = ["a", "c"]
assert test(dictA, str0) == expected_output, 'Test failed'