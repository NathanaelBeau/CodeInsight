lst0 = [10, 20, 30, 40]
lst1 = [
            {"name": "John", "eyecolor": 40},
            {"name": "Alice", "eyecolor": 10},
            {"name": "Bob", "eyecolor": 20},
            {"name": "Eve", "eyecolor": 30}
        ]
var0 = "eyecolor"
expected_output = [
            {"name": "Alice", "eyecolor": 10},
            {"name": "Bob", "eyecolor": 20},
            {"name": "Eve", "eyecolor": 30},
            {"name": "John", "eyecolor": 40}
        ]
assert test(lst0, lst1, var0) ==expected_output, 'Test failed'