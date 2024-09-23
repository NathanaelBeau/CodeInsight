var0 = "[First] and [second] brackets."
expected_result =  "First"  # Only retrieves the first match.
result = test(var0)
assert result == expected_result, 'Test failed'