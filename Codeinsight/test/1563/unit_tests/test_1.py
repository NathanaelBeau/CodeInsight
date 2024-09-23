# Test 2
data = {
            'A': [1, 2, 3, 4],
            'B': [10, 20, 30, 40],
            'C': [5, 15, 25, 35]
        }
df = pd.DataFrame(data)
result = test(df, 'df0["A"] > 10')
expected = pd.DataFrame(columns=['A', 'B', 'C'], dtype='int64')
if pd.testing.assert_frame_equal(result, expected) is not None:
    assert False, 'Test failed'
