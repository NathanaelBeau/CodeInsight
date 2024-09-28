arr0 = np.array([[10, 20], [30, 40], [50, 60]])
lst0 = [1]
lst1 = [0]
expected_result =  np.array([[30]])
assert np.array_equal(test(arr0, lst0, lst1), expected_result), 'Test failed'