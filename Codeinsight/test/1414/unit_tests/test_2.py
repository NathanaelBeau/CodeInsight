var0 = np.array([[1, 2],
                         [3, 4]])
new_cols = np.array([[5, 6],
                             [7, 8]])
expected = np.array([[1, 2, 5, 6],
                             [3, 4, 7, 8]])
result = test(var0, slice(None, None), slice(None, None), None, extend_cols=new_cols)
if np.testing.assert_array_equal(result, expected) is not None:
    assert False, 'Test failed'  # This will never be reached if the assertion passes.