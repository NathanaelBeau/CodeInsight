lst0 = ["blue", "green", "red"]
lst1 = [
            {"name": "John", "eyecolor": "red"},
            {"name": "Alice", "eyecolor": "blue"},
            {"name": "Bob", "eyecolor": "green"}
        ]
var0 = "eyecolor"
expected_output = [
            {"name": "Alice", "eyecolor": "blue"},
            {"name": "Bob", "eyecolor": "green"},
            {"name": "John", "eyecolor": "red"}
        ]
assert test(lst0, lst1, var0) ==expected_output, 'Test failed'