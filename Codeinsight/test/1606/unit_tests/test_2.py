arg0 = np.array([3, 3, 3])
arg1 = np.array([1, 2])
expected_output = np.array([[3, 6], [3, 6], [3, 6]])
assert (test(arg0,arg1)  == expected_output).all(), 'Test failed'