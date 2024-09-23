var0 = r'[!?.]'
var1 = "Hello! How are you? Good."
expected_result =  ["Hello", " How are you", " Good", ""]
result = test(var0, var1)
assert result == expected_result, 'Test failed'