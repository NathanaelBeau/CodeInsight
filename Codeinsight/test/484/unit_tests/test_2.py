str0 = "1;2;3;4;5"
lst0 = [";"]
expected_output = ["1", "2", "3", "4", "5"]
assert test(str0, lst0) ==expected_output, 'Test failed'