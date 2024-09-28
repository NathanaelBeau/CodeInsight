var0 = "Hello\nWorld!\nHello again."
expected_result =  ['\n', '\n']
result = test(var0)
assert result == expected_result, 'Test failed'