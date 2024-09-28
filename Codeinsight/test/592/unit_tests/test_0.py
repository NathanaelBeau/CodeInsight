lst0 = ["some_string,1.2,3.4,5.6,another_string"]
expected_output = [1.2, 3.4, 5.6]
assert test(lst0) ==expected_output, 'Test failed'