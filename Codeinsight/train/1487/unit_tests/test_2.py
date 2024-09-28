data = {
    'Category': ['A', 'B', 'A', 'B', 'C'],
    'Value': [10, 20, 30, 40, 50]
}
df = pd.DataFrame(data)
expected_c = df[df['Category'] == 'C'].reset_index(drop=True)
result_c = test(df, 'Category', 'C')
if pd.testing.assert_frame_equal(result_c.reset_index(drop=True), expected_c) is not None:
    assert False, 'Test failed'
