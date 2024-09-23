arr3 = np.array([[1, 2],
                     [2, 3],
                     [3, 4]])
expected3 = np.array([[1, 2],
                           [2, 3],
                           [3, 4]])
if np.testing.assert_array_equal(test(arr3), expected3) is not None:
    assert False, 'Test failed'
