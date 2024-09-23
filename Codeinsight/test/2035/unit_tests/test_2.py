s3 = "apple, orange, apple!"
pattern3 = r"apple"
expected_output3 = ["apple", "apple"]
assert test(s3, pattern3) == expected_output3, 'Test failed'