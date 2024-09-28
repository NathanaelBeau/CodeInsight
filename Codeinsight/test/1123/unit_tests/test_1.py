df2 = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
result2 = test(df2, 'RowIndex')
expected2 = pd.DataFrame({'A': [1, 2], 'B': [3, 4], 'RowIndex': [0, 1]})
if pd.testing.assert_frame_equal(result2, expected2) is not None:
    assert False, 'Test failed'