var0 = "FirstLine\n\nSecondLine\nThirdLine"
expected_result =  [("FirstLine", "\nSecondLine\nThirdLine")]
result = test(var0)
assert result == expected_result, 'Test failed'