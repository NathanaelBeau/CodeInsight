str0 = '00000001000000ff00'
expected_output = [0, 0, 0, 1, 0, 0, 0, 255, 0]
assert test(str0) == expected_output, 'Test failed'