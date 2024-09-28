str0 = '\x00\xff\x00\xff\x00\xff'
expected_output = [0, 255, 0, 255, 0, 255]
assert test(str0) == expected_output, 'Test failed'