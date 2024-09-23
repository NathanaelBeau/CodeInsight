df0 = pd.DataFrame({
            'A': [np.nan, np.nan],
            'B': [np.nan, np.nan]
        })
result = test(df0)
expected_df = pd.DataFrame({
            'A': [np.nan, np.nan],
            'B': [np.nan, np.nan]
        })
if not pd.testing.assert_frame_equal(result, expected_df) is None:
    assert 'Test failed'
