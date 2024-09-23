lst0 = [10, 20, 30, 40]
lst1 = [
            {"name": "John", "score": 40},
            {"name": "Alice", "score": 10},
            {"name": "Bob", "score": 20},
            {"name": "Eve", "score": 30}
        ]
var0 = "score"
expected_output = [
            {"name": "Alice", "score": 10},
            {"name": "Bob", "score": 20},
            {"name": "Eve", "score": 30},
            {"name": "John", "score": 40}
        ]
assert test(lst0, lst1, var0 ) ==expected_output, 'Test failed'