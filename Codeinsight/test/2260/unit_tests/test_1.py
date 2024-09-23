var0 = "Python! 你好"
expected_result =  "Python! \\u4f60\\u597d"
result = test(var0)
assert result == expected_result, 'Test failed'