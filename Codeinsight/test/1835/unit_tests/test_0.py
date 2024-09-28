lst0 = ["1.1.2", "1.0.0", "1.3.3", "1.0.12", "1.0.2"]
expected_output = ["1.0.0", "1.0.2", "1.0.12", "1.1.2", "1.3.3"]
assert test(lst0) == expected_output, 'Test failed'