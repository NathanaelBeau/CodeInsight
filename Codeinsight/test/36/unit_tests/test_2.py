str0 = '00ff00ff00ff'
expected_output = [0, 255, 0, 255, 0, 255]
assert test(str0) == expected_output, 'Test failed'