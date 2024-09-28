s3 = "No-symbols! Or... maybe^some?"
expected_output3 = 'NosymbolsOrmaybesome'
assert test(s3) == expected_output3, 'Test failed'