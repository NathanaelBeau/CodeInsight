lst0 = [1, 2, 1, 3, 2, 4, 5, 4]
expected_output = {1: {'id': 1, 'position': 2},
                           2: {'id': 2, 'position': 4},
                           3: {'id': 3, 'position': 3},
                           4: {'id': 4, 'position': 7},
                           5: {'id': 5, 'position': 6}}
assert test(lst0) ==expected_output, 'Test failed'