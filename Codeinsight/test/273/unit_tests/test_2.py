binary_str0 = '0100000011101101001001000000000000000000000000000000000000000000'  # Represents 1.234567e300
expected_output = 59680.0
assert test(binary_str0) == expected_output, 'Test failed'