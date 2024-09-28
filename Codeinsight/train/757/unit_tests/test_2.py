s3 = "apple...banana....orange.....grape"
pattern3 = "\.{2,}"
expected_output3 = [(5, 8, '...'), (14, 18, '....'), (24, 29, '.....')]
assert test(s3, pattern3) == expected_output3, 'Test failed'