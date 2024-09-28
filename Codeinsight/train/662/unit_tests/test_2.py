s3 = "apple apple-apple apple_apple"
pattern3 = "apple"
expected_output3 = [0, 6, 12, 18, 24]
assert test(s3, pattern3) == expected_output3, 'Test failed'