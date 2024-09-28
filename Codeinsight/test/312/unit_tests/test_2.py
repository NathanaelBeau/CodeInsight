arr0 = np.array([[1, 1.], [2, 1.], [3, 2.], [4, 2.], [5, 1.], [6, 1.]])
expected_output = np.array([2, 4])
assert (test(arr0)  ==  expected_output).all(), 'Test failed'