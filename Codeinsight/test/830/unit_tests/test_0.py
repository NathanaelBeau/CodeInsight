s1 = "Hello 123 world 456"
pattern1 = r"\d+"  # matches one or more digits
replacement1 = "NUM"
expected_output1 = "Hello NUM world NUM"
assert test(s1, pattern1, replacement1) == expected_output1, 'Test failed'