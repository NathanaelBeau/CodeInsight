var0 = "apple,banana,grape,,orange"
expected_result =  ["apple", "banana", "grape", "0", "orange"]
result = test(var0)
assert result == expected_result, 'Test failed'