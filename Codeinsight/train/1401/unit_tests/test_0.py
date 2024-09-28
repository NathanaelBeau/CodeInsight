df1 = pd.DataFrame({
        'group': ['A', 'A', 'B', 'B', 'C'],
        'value': [10, 20, 5, 30, 25],
        'name': ['a1', 'a2', 'b1', 'b2', 'c1']
    })
expected_1 = pd.DataFrame({
        'group': ['A', 'B', 'C'],
        'value': [20, 30, 25],
        'name': ['a2', 'b2', 'c1']
    })
result_1 = test(df1, 'group', 'value')
if pd.testing.assert_frame_equal(result_1, expected_1) is not None:
    assert False, 'Test failed'