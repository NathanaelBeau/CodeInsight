str0 = "(First) This is a (test) string."
expected_result =  " This is a  string."
result = test(str0)
assert result == expected_result, 'Test failed'