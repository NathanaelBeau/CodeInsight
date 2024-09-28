df1 = pd.DataFrame({
    'A': ['1', '2', 'three'],
    'B': ['4', 'five', '6'],
    'C': ['7.1', '8.2', 'nine']
})
result_1 = test(df1)
expected_1 = pd.DataFrame({
    'A': [1.0, 2.0, np.nan],
    'B': [4.0, np.nan, 6.0],
    'C': [7.1, 8.2, np.nan]
})
if pd.testing.assert_frame_equal(result_2, expected_2, check_dtype=False) is not None:
    assert False, 'Test failed'
