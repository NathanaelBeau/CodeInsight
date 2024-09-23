s1 = "The rain in Spain falls mainly on the plain."
pattern1 = r"\b\w+ain\b"  # matches words ending with "ain"
expected_output1 = ["rain", "Spain", "plain"]
assert test(s1, pattern1) == expected_output1, 'Test failed'