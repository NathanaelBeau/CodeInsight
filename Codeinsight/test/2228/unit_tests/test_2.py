df2 = pd.DataFrame({
        'group': ['X', 'X', 'Y', 'Y'],
        'value': [50, 50, 40, 100],
        'name': ['x1', 'x2', 'y1', 'y2']
    })
expected_2 = pd.DataFrame({
        'group': ['X', 'Y'],
        'value': [50, 100],
        'name': ['x1', 'y2']
    })
result_2 = test(df2, 'group', 'value')
if pd.testing.assert_frame_equal(result_2, expected_2) is not None:
    assert False, 'Test failed'