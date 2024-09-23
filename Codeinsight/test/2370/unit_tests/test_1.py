data = {
    'Category': ['A', 'B', 'A', 'B', 'C'],
    'Value': [10, 20, 30, 40, 50]
}
df = pd.DataFrame(data)
expected_b = df[df['Category'] == 'B'].reset_index(drop=True)
result_b = test(df, 'Category', 'B')
if pd.testing.assert_frame_equal(result_b.reset_index(drop=True), expected_b) is not None:
    assert False, 'Test failed'
