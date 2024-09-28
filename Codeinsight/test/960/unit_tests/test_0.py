var0 = "Hello world! Good world!"
replacements = {"world": "planet", "Good": "Great"}
expected_result =  "Hello planet! Great planet!"
result = test(var0, replacements)
assert result == expected_result, 'Test failed'