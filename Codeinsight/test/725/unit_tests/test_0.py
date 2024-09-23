s1 = "Hello@world! How^are&you?"
expected_output1 = 'HelloworldHowareyou'
assert test(s1) == expected_output1, 'Test failed'