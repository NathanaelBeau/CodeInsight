var0 = ",,apple,banana,grape,orange,,"
expected_result =  ["0", "0", "apple", "banana", "grape", "orange", "0", "0"]
result = test(var0)
assert result == expected_result, 'Test failed'