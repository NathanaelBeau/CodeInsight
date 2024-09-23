lst0 = [{'weight': 1, 'factor': 7}, {'weight': 3, 'factor': 2}, {'weight': 2, 'factor': 4}]
expected_output = [{'weight': 1, 'factor': 7}, {'weight': 2, 'factor': 4}, {'weight': 3, 'factor': 2}]
assert test(lst0) ==expected_output, 'Test failed'