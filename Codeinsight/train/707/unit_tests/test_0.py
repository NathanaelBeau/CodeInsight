dict0 = { "apple": "fruit", "carrot": "vegetable", "banana": "fruit", "broccoli": "vegetable" }
var0 = "I like to eat apple and carrot. Banana and broccoli are also good."
expected_output = "I like to eat fruit and vegetable. fruit and vegetable are also good."
assert test(dict0, var0) ==expected_output, 'Test failed'