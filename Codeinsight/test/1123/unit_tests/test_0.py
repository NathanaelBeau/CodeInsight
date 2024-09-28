df1 = pd.DataFrame({'A': [10, 20, 30]})
result1 = test(df1, 'Index')
expected1 = pd.DataFrame({'A': [10, 20, 30], 'Index': [0, 1, 2]})
if pd.testing.assert_frame_equal(result1, expected1) is not None:
    assert False, 'Test failed'