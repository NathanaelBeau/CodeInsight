s1 = "apple, banana; orange, grape"
pattern1 = "[,;]"
expected_output1 = ['apple', ' banana', ' orange', ' grape']
assert test(s1, pattern1) == expected_output1, 'Test failed'