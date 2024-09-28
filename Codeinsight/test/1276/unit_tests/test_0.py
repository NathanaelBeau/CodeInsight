lst0 = [{'weight': 10, 'factor': 3}, {'weight': 5, 'factor': 2}, {'weight': 8, 'factor': 4}]
expected_output = [{'weight': 5, 'factor': 2}, {'weight': 8, 'factor': 4}, {'weight': 10, 'factor': 3}]
assert test(lst0) ==expected_output, 'Test failed'