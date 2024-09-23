df2 = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4.0, 5.5, 6.1]
})
result_2 = test(df2)
expected_2 = df2
if pd.testing.assert_frame_equal(result_2, expected_2, check_dtype=False) is not None:
    assert False, 'Test failed'
