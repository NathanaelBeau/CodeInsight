data_test_1 = {
    'A': [10, 20, 30],
    'B': [2, 4, 6],
    'C': [1, 2, 3]
}
df_test_1 = pd.DataFrame(data_test_1)
result_1 = test(df_test_1.copy(), ['A', 'B'], 'C')
expected_1 = pd.DataFrame({
    'A': [10.0, 10.0, 10.0],
    'B': [2.0, 2.0, 2.0],
    'C': [1, 2, 3]
})
if pd.testing.assert_frame_equal(result_1.reset_index(drop=True), expected_1.reset_index(drop=True)) is not None:
    assert False, 'Test failed'