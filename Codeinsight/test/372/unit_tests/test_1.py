s2 = "123abc 456def 789ghi"
pattern2 = r"\d+"  # matches sequences of digits
expected_output2 = ["123", "456", "789"]
assert test(s2, pattern2) == expected_output2, 'Test failed'