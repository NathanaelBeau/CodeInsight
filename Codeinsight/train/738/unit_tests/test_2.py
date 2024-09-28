str0 = "3:6"
lst0 = [True, 1, "apple", 3.14, "banana", 42, None]
expected_result3 = [3.14, "banana", 42]
result3 = test(str0, lst0)
assert test(str0, lst0) ==expected_result3, 'Test failed'