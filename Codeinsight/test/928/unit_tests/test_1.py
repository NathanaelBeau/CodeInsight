arr0 = np.array([[1, 1.], [2, 2.], [3, 3.], [4, 4.], [5, 5.]])
expected_output = np.array([1, 2, 3, 4])
assert (test(arr0)  ==  expected_output).all(), 'Test failed'