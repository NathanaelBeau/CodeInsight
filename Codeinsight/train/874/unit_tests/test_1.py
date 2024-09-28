s2 = "apple, orange, apple!"
pattern2 = r"apple"
replacement2 = "banana"
expected_output2 = "banana, orange, banana!"
assert test(s2, pattern2, replacement2) == expected_output2, 'Test failed'