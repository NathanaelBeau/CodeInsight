arg0 = np.array([1, 2])
arg1 = np.array([3, 4])
expected_output = np.array([[3, 4], [6, 8]])
assert (test(arg0,arg1)  == expected_output).all(), 'Test failed'