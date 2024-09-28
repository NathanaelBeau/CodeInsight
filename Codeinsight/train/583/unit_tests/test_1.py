var0 = "apple,  banana\tcherry"
expected_result =  ["apple,", "banana", "cherry"]
result = test(var0)
assert result == expected_result, 'Test failed'