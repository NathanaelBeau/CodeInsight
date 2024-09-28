str0 = '\u2600' # Unicode for SUN symbol
expected_result =  b'\xe2\x98\x80'
assert test(str0) == expected_result, 'Test failed'