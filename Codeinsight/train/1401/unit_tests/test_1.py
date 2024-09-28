df3 = pd.DataFrame({
        'group': ['Z', 'Z'],
        'value': [15, 25],
        'name': ['z1', 'z2']
    })
expected_3 = pd.DataFrame({
        'group': ['Z'],
        'value': [25],
        'name': ['z2']
    })
result_3 = test(df3, 'group', 'value')
if pd.testing.assert_frame_equal(result_3, expected_3) is not None:
    assert False, 'Test failed'