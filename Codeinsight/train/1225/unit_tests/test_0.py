data_test_1 = {
    'date': pd.to_datetime(['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04']),
    'value': [10, 20, 30, 40]
}
df_test_1 = pd.DataFrame(data_test_1)
result_1 = test(df_test_1, 'date', '2023-01-01', '2023-01-04')
expected_1 = df_test_1.iloc[1:3]  # Should return rows 1 and 2
if pd.testing.assert_frame_equal(result_1.reset_index(drop=True), expected_1.reset_index(drop=True)) is not None:
    assert False, 'Test failed'
