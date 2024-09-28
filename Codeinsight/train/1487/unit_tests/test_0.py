data = {
    'Category': ['A', 'B', 'A', 'B', 'C'],
    'Value': [10, 20, 30, 40, 50]
}
df = pd.DataFrame(data)
expected_a = df[df['Category'] == 'A'].reset_index(drop=True)
result_a = test(df, 'Category', 'A')
if pd.testing.assert_frame_equal(result_a.reset_index(drop=True), expected_a) is not None:
    assert False, 'Test failed'
