var2 = "startExample text.close"
pattern2 = r"(?<=start).*(?=close)"
expected_output3 = "Example text."
assert test(var2, pattern2) == expected_output3, 'Test failed'