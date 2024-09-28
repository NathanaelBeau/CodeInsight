var0 = "apple, banana, cherry"
replacements = {"apple": "grape", "cherry": "peach"}
expected_result =  "grape, banana, peach"
result = test(var0, replacements)
assert result == expected_result, 'Test failed'