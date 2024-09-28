s3 = "a1b2c3"
pattern3 = r"\d"
replacement3 = "X"
expected_output3 = "aXbXcX"
assert test(s3, pattern3, replacement3) == expected_output3, 'Test failed'