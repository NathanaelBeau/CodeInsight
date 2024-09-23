arr1 = np.array([[3, 1, 2],
                     [4, 2, 1],
                     [1, 3, 4]])
expected1 = np.array([[1, 1, 1],
                           [3, 2, 2],
                           [4, 3, 4]])
if np.testing.assert_array_equal(test(arr1), expected1) is not None:
    assert False, 'Test failed'
