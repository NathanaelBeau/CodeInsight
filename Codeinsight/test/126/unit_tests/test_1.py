lst0 = [np.array([10, 20,60]), np.array([30, 40, 50])]
expected_output = np.array([10, 20, 60, 30, 40, 50])
assert (test(lst0)  == expected_output).all(), 'Test failed'