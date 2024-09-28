string1 = "Hello**World***Python****!"
expected_output1 = "Hello*World*Python*!"
assert test(string1) == expected_output1, 'Test failed'