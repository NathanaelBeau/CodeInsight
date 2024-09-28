arr0 = np.array([10, 20, 30, 40])
expected_output= np.array([[10, 20], [30, 40]])
assert (test(arr0)  == expected_output).all(), 'Test failed'