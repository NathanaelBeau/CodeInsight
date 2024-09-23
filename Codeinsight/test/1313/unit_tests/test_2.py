lst0 = ["Steve", "Steve", "Ben", "Ben", "Steve"]
dict0 = {"Steve": "Blue", "Ben": "Red"}
expected_output = ["Blue", "Blue", "Red", "Red", "Blue"]
assert test(lst0, dict0 ) ==expected_output, 'Test failed'