input_str = "Line 1\n\nLine 2\n\nLine 3"
expected = ['Line 1', 'Line 2', 'Line 3']
assert test(input_str) ==expected, 'Test failed'