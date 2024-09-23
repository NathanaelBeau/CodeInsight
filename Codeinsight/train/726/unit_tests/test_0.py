str0 = "(1,2,3)"
tpl0 = (4,5,6)
expected_result =  (4,5,6,1,2,3)
result = test(str0, tpl0)
assert result == expected_result, 'Test failed'