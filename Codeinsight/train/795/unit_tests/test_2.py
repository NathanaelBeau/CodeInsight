arr0 = np.array([100, 200])
arr1 = np.array([300, 400])
expected_output = np.array([100, 300, 200, 400])
assert (test(arr0,arr1)  == expected_output).all(), 'Test failed'