df4 = pd.DataFrame({'A': [100, 200]}, index=[5, 10])
result4 = test(df4, 'NewIndex')
expected4 = pd.DataFrame({'A': [100, 200], 'NewIndex': [5, 10]}, index=[5, 10])
if pd.testing.assert_frame_equal(result4, expected4) is not None:
    assert False, 'Test failed'