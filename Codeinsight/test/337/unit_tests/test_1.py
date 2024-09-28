lst0 = ["0.01", "0.1", "0.001", "1.0", "0.0001"]
expected_output = ["0.0001", "0.001", "0.01", "0.1", "1.0"]
assert test(lst0) ==expected_output, 'Test failed'