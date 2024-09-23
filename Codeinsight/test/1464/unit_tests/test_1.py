arg0 = np.array([1, 1])
arg1 = np.array([0, 0])
expected_output = np.array([[0, 0], [0, 0]])
assert (test(arg0,arg1)  == expected_output).all(), 'Test failed'