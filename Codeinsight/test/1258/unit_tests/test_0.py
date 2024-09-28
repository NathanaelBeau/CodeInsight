arr1 = np.array([[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9]])
result_1 = test(arr1, slice(0, 2), slice(1, 3), 2)
expected_1 = np.array([[2, 3],
                       [5, 6],
                       [5, 6],
                       [5, 6]])
if np.testing.assert_array_equal(result_1, expected_1) is not None:
    assert False, 'Test failed'
