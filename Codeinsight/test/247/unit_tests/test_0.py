var0 = np.array([[1, 2, 3, 4],
                         [5, 6, 7, 8],
                         [9, 10, 11, 12],
                         [13, 14, 15, 16]])
expected = np.array([[ 6,  7],
                             [10, 11],
                             [17, 18],
                             [19, 20]])
result = test(var0, slice(1, 3), slice(1, 3), np.array([[17, 18], [19, 20]]), None)
if np.testing.assert_array_equal(result, expected) is not None:
    assert False, 'Test failed'  # This will never be reached if the assertion passes.