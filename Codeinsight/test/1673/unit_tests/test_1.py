lst0 = [np.array([10, 20]), np.array([30, 40, 50]), np.array([60])]
expected_output = np.array([10, 20, 30, 40, 50, 60])
assert (test(lst0)  == expected_output).all(), 'Test failed'