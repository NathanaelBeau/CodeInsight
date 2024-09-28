str0 = '\x00\x00\x00\x01\x00\x00\x00\xff\xff\x00\x00'
expected_output = [0, 0, 0, 1, 0, 0, 0, 255, 255, 0, 0]
assert test(str0) == expected_output, 'Test failed'