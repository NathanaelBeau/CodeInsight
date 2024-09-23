str0 = "Hello,world;how|are+you"
lst0 = [",", ";", "|", "+"]
expected_output = ["Hello", "world", "how", "are", "you"]
assert test(str0, lst0) ==expected_output, 'Test failed'