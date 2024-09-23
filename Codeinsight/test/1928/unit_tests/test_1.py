data_test_2 = {
    'date': pd.to_datetime(['2023-01-01', '2023-01-02']),
    'value': [10, 20]
}
df_test_2 = pd.DataFrame(data_test_2)
result_2 = test(df_test_2, 'date', '2023-01-03', '2023-01-05')
expected_2 = pd.DataFrame(columns=['date', 'value'])  # Should return empty DataFrame
if pd.testing.assert_frame_equal(result_1.reset_index(drop=True), expected_1.reset_index(drop=True)) is not None:
    assert False, 'Test failed'