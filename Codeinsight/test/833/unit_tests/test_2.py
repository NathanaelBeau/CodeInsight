lst0 = ["Test\r\n", "this\r\n", "method\r\n"]
expected_output = ["Test", "this", "method"]
assert test(lst0) == expected_output, 'Test failed'