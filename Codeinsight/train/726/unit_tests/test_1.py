str0 = "7,8,9"
tpl0 = (10, 11, 12)
expected_result =  (10, 11, 12, 7, 8, 9)
result = test(str0, tpl0)
assert result == expected_result, 'Test failed'