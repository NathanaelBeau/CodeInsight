tpl0 = (True, False, 1, 'a')
expected_result =  "TrueFalse1a"
result = test(tpl0)
assert result == expected_result, 'Test failed'