dict0 = { "red": "color", "blue": "color", "yellow": "color" }
var0 = "I love the colors Red, BLUE, and YELLOW."
expected_output = "I love the colors color, color, and color."
assert test(dict0, var0) ==expected_output, 'Test failed'