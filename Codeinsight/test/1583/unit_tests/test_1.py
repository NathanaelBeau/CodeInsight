arr0 = np.array([1, 2, 3, 8, 9, 10])
labels = test(arr0, 1)
expected_labels = np.array([0, 0, 0, 0, 0, 0])
assert (labels  ==  expected_labels).all(), 'Test failed'