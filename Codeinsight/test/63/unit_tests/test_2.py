lst0 = ["5.5.5", "2.0.0", "3.3.3", "1.1.1"]
expected_output = ["1.1.1", "2.0.0", "3.3.3", "5.5.5"]
assert test(lst0) == expected_output, 'Test failed'