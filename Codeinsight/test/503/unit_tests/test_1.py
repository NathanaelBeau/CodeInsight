df = pd.DataFrame({
            'Category': ['A', 'A', 'B', 'B', 'C'],
            'Values': [10, 20, 10, 30, 50]
        })
result = test(df, str0='Category', str1='Values')
expected = pd.DataFrame({
            'Mean': [15.0, 20.0, 50.0],
            'Sum': [30, 40, 50]
        }, index=['A', 'B', 'C'])
expected.index.name = 'Category'
if pd.testing.assert_frame_equal(result,expected) is not None:
    assert False, 'Test failed'