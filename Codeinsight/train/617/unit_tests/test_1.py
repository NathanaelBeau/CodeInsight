lst0 = [
        [4, 5],
        ['x', 'y', 'z'],
        [0.1, 0.2, 0.3]
        ]
expected_output = [('4', 'x', '0.1'), ('4', 'y', '0.1'), ('4', 'z', '0.1'), ('5', 'x', '0.1'), ('5', 'y', '0.1'), ('5', 'z', '0.1'), ('4', 'x', '0.2'), ('4', 'y', '0.2'), ('4', 'z', '0.2'), ('5', 'x', '0.2'), ('5', 'y', '0.2'), ('5', 'z', '0.2'), ('4', 'x', '0.3'), ('4', 'y', '0.3'), ('4', 'z', '0.3'), ('5', 'x', '0.3'), ('5', 'y', '0.3'), ('5', 'z', '0.3')]
assert test(lst0) ==expected_output, 'Test failed'