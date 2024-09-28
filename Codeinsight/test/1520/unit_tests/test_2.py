df0 = pd.DataFrame()
result = test(df0)
if not pd.testing.assert_frame_equal(result, df0) is None:
    assert 'Test failed'