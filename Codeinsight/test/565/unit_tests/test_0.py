lst0 = [1, 2, 3, 4, 5]
expected_output = {1: {'id': 1, 'position': 0},
                           2: {'id': 2, 'position': 1},
                           3: {'id': 3, 'position': 2},
                           4: {'id': 4, 'position': 3},
                           5: {'id': 5, 'position': 4}}
assert test(lst0) ==expected_output, 'Test failed'