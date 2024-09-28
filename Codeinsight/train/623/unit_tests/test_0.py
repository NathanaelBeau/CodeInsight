arr0 = np.array(['x', 'y', 'z'])
expected_output = [{'x': 'x'}, {'x': 'y'}, {'x': 'z'}]
assert test(arr0) == expected_output, 'Test failed'