str0 = "abcabc"
expected_result =  ['a', 'b', 'c']
result = sorted(test(str0))
assert result==expected_result, 'Test failed'