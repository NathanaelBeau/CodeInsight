var0 = "This is a\t text\nwith multiple   spaces"
expected_result =  ["This", "is", "a", "text", "with", "multiple", "spaces"]
result = test(var0)
assert result == expected_result, 'Test failed'