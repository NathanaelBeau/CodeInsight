arr0 = np.array([1.1, 2.2, 3.3, 8.8, 9.9, 10.1])
labels = test(arr0, 2)
expected_labels = np.array([1, 1, 1, 0, 0, 0])
assert (labels  ==  expected_labels).all(), 'Test failed'