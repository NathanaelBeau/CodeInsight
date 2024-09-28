str0 = "(7.0, 8.1)"
tpl0 = (9.2, 10.3)
expected_result =  (9.2, 10.3, 7.0, 8.1)
result = test(str0, tpl0)
assert result == expected_result, 'Test failed'