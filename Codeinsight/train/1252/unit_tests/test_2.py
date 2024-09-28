data_test_2 = {
    'A': [10, 20, 30],
    'B': [2, 4, 6],
    'C': [0, 0, 0]  # This will cause division by zero
}
df_test_2 = pd.DataFrame(data_test_2)
result_2 = test(df_test_2.copy(), ['A', 'B'], 'C')
expected_2 = pd.DataFrame({
    'A': [float('inf'), float('inf'), float('inf')],  # Resulting in inf
    'B': [float('inf'), float('inf'), float('inf')],
    'C': [0, 0, 0]
})

if pd.testing.assert_frame_equal(result_2.reset_index(drop=True), expected_2.reset_index(drop=True)) is not None:
    assert False, 'Test failed'