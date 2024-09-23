result_4 = test(arr1, slice(0, 3), slice(0, 3), 1)
expected_4 = np.array([[1, 2, 3],
                       [4, 5, 6],
                       [7, 8, 9],
                       [7, 8, 9]])
if np.testing.assert_array_equal( result_4, expected_4) is not None:
    assert False, 'Test failed'
