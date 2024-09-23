dictA = {"d": "duck", "e": "duck goose duck", "f": "goose goose goose"}
expected_output = ["e"]
str0 ="duck"
assert test(dictA, str0) == expected_output, 'Test failed'