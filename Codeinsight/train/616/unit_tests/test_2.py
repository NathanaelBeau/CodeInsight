lst0 = [100, 200, 300, 400]
expected_output = {100: {'id': 100, 'position': 0},
                           200: {'id': 200, 'position': 1},
                           300: {'id': 300, 'position': 2},
                           400: {'id': 400, 'position': 3}}
assert test(lst0) ==expected_output, 'Test failed'