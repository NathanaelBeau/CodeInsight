var0 = "f"
dct0 = {"a": 1, "b": {"c": 2, "d": {"e": 4, "f": 5}}}
expected_result =  5
result = test(var0, dct0)
assert result == expected_result, 'Test failed'