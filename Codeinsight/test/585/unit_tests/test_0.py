s1 = "apple banana apple orange"
pattern1 = "apple"
expected_output1 = [(0, 5, 'apple'), (13, 18, 'apple')]
assert test(s1, pattern1) == expected_output1, 'Test failed'