var0 = "Line1\n\nLine2\nLine3\nLine4"
expected_result =  [("Line1", "\nLine2\nLine3\nLine4")]
result = test(var0)
assert result == expected_result, 'Test failed'