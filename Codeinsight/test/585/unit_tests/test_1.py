s2 = "1a23b456c"
pattern2 = "\d+"
expected_output2 = [(0, 1, '1'), (2, 4, '23'), (5, 8, '456')]
assert test(s2, pattern2) == expected_output2, 'Test failed'