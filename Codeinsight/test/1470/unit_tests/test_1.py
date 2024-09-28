lst0 = [{"name": "venus", "type": "planet"}, {"name": "pluto", "type": "ex-planet"}, {"name": "moon", "type": "satellite"}]
var0 = "pluto"
expected_output = {"name": "pluto", "type": "ex-planet"}
assert test(lst0, var0) == expected_output, 'Test failed'