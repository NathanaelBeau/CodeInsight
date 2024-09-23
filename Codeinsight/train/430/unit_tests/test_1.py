s2 = "A1 B2 C3 D4 E5"
pattern2 = r"\d"
expected_output2 = [1, 4, 7, 10, 13]
assert test(s2, pattern2) == expected_output2, 'Test failed'