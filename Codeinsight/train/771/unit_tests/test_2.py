var0 = "I need to get groceries and get some rest."
expected_result =  "I need to get@ groceries and get@ some rest."
result = test(var0)
assert result == expected_result, 'Test failed'