lst0 = [1, 2, 3, 4]
expected_output = {((3, 4), (1, 2)), ((3, 1), (2, 4)), ((2, 3), (1, 4)), ((4, 3), (1, 2)), ((4, 3), (2, 1)), ((2, 3), (4, 1)), ((2, 1), (4, 3)), ((1, 3), (4, 2)), ((3, 2), (1, 4)), ((3, 1), (4, 2)), ((1, 4), (2, 3)), ((3, 4), (2, 1)), ((4, 2), (1, 3)), ((4, 2), (3, 1)), ((1, 4), (3, 2)), ((2, 4), (1, 3)), ((4, 1), (2, 3)), ((2, 4), (3, 1)), ((1, 3), (2, 4)), ((3, 2), (4, 1)), ((4, 1), (3, 2)), ((1, 2), (4, 3)), ((1, 2), (3, 4)), ((2, 1), (3, 4))}
assert test(lst0) ==expected_output, 'Test failed'