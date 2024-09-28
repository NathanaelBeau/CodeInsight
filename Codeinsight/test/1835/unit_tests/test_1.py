lst0= ["1.0.0", "2.0.0", "1.0.0"]
expected_output = ["1.0.0", "1.0.0", "2.0.0"]
assert test(lst0) == expected_output, 'Test failed'