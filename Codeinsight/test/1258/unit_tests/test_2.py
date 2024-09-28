result_2 = test(arr1, slice(1, 3), slice(0, 2), 0)
expected_2 = np.array([[4, 5],
                       [7, 8]])
if np.testing.assert_array_equal(result_2, expected_2) is not None:
    assert False, 'Test failed'
