var1 = "beginThis is a sample.end"
pattern1 = r"(?<=begin).*(?=end)"
expected_output2 = "This is a sample."
assert test(var1, pattern1) == expected_output2, 'Test failed'