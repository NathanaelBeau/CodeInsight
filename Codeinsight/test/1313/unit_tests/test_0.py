lst0 = ["Steve", "Steve", "Ben", "Ben", "Johnny"]
dict0 = {"Steve": "Blue", "Ben": "Red", "Johnny": "Green"}
expected_output = ["Blue", "Blue", "Red", "Red", "Green"]
assert test(lst0, dict0 ) ==expected_output, 'Test failed'