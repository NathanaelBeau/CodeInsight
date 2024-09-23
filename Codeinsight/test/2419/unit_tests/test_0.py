parent_dict = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five'}
expected_output = {2: 'two', 3: 'three', 4: 'four'}
assert test(parent_dict) == expected_output, 'Test failed'