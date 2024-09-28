lst0 = ["value,1.0,2.0,3.0, value"]
expected_output = [1.0, 2.0, 3.0]
assert test(lst0) ==expected_output, 'Test failed'