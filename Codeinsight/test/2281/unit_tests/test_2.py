s3 = "No special characters here!"
expected_output3 = 'No\ special\ characters\ here!'
assert test(s3) == expected_output3, 'Test failed'