str0 = '\xc5\xc4\xd6'
expected_result =  b'\xc3\x85\xc3\x84\xc3\x96'
assert test(str0) == expected_result, 'Test failed'