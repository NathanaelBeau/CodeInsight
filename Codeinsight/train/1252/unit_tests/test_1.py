data_test_4 = {
    'A': [5],
    'B': [10],
    'C': [2]
}
df_test_4 = pd.DataFrame(data_test_4)
result_4 = test(df_test_4.copy(), ['A', 'B'], 'C')
expected_4 = pd.DataFrame({
    'A': [2.5],
    'B': [5.0],
    'C': [2]
})

if pd.testing.assert_frame_equal(result_4.reset_index(drop=True), expected_4.reset_index(drop=True)) is not None:
    assert False, 'Test failed'