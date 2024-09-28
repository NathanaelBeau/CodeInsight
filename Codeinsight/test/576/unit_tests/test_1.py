data = {
            'A': [1., 2., np.nan, 4.],
            'B': [5., np.nan, 7., 8.],
            'C': [np.nan, np.nan, 11., 12.]
        }
df0 = pd.DataFrame(data)
result = test(df0)
expected_data = {
            'A': [1.0, 2.0, 2.33, 4.0],
            'B': [5.0, 6.67, 7.0, 8.0],
            'C': [11.5, 11.5, 11.0, 12.0]
        }
expected_df = pd.DataFrame(expected_data)
if not pd.testing.assert_frame_equal(result, expected_df, rtol=1e-2) is None:
    assert 'Test failed'