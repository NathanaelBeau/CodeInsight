# Test 2: Single column
arr2 = np.array([[3],
                 [1],
                 [2]])
expected2 = np.array([[1],
                      [2],
                      [3]])
if np.testing.assert_array_equal(test(arr2), expected2) is not None:
    assert False, 'Test failed'
