lst0 = ["Hello\r\n", "World\r\n", "Example\r\n"]
expected_output = ["Hello", "World", "Example"]
assert test(lst0) == expected_output, 'Test failed'