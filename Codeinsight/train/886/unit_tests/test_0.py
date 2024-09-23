lst0 = np.array([2,3,4,5,6])
lst1 = np.array([0.1, 0.2, 0.3, 0.2, 0.2])
expected_output = np.sqrt(np.average((lst0-np.average(lst0, weights=lst1))**2, weights=lst1))
assert test(lst0, lst1) == expected_output, 'Test failed'