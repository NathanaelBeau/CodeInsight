arr0 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
original_contents = arr0.copy()
result = test(arr0)
assert np.array_equal(np.sort(original_contents, axis=0), np.sort(result, axis=0)), 'Test failed'