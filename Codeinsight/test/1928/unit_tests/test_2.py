data_test_3 = {
    'date': pd.to_datetime(['2023-01-01', '2023-01-02', '2023-01-03']),
    'value': [10, 20, 30]
}
df_test_3 = pd.DataFrame(data_test_3)
result_3 = test(df_test_3, 'date', '2023-01-01', '2023-01-03')
expected_3 = df_test_3.iloc[1:2]  # Should return row 1 (2023-01-02)
if pd.testing.assert_frame_equal(result_1.reset_index(drop=True), expected_1.reset_index(drop=True)) is not None:
    assert False, 'Test failed'