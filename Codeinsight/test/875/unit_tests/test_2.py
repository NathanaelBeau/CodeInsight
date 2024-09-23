str0 = b'\xc2\xa92023'
expected_result =  '©2023'
result = test(str0)
assert result == expected_result, 'Test failed'