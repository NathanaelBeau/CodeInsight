lst0 = np.array([5, 6, 7])
lst1 = np.array([5, 7, 7])
expected_output = 0.3333333333333333  
assert test(lst0, lst1) == expected_output, 'Test failed'