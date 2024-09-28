arr0 = np.array([[10, 20], [30, 40], [50, 60], [70, 80]])
original_contents = arr0.copy()
result = test(arr0)
assert np.array_equal(np.sort(original_contents, axis=0), np.sort(result, axis=0)), 'Test failed'