lst0 = [{"name": "mars", "type": "planet"}, {"name": "saturn", "type": "planet"}, {"name": "pluto", "type": "planet"}]
var0 = "pluto"
expected_output = {"name": "pluto", "type": "planet"}
assert test(lst0, var0) == expected_output, 'Test failed'