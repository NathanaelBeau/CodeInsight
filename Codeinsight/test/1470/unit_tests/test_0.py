lst0 = [{"name": "earth", "type": "planet"}, {"name": "pluto", "type": "dwarf planet"}, {"name": "sun", "type": "star"}]
var0 = "pluto"
expected_output = {"name": "pluto", "type": "dwarf planet"}
assert test(lst0, var0) == expected_output, 'Test failed'