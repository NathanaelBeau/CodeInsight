s3 = "apple...banana....orange.....grape"
pattern3 = "\.{2,}"
expected_output3 = ['apple', 'banana', 'orange', 'grape']
assert test(s3, pattern3) == expected_output3, 'Test failed'