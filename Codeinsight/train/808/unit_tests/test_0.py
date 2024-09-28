str0 = "Hello"
lst0 = ["Alice", "Bob", "Charlie"]
expected_result =  ["HelloAlice", "HelloBob", "HelloCharlie"]
result = test(str0, lst0)
assert result == expected_result, 'Test failed'