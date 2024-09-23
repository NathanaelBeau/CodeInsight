df0 = pd.DataFrame({
            'A': [0, 1, 2],
            'B': [0, 0, 0],
            'C': [3, 4, 5]
        })
expected = pd.DataFrame({
            'A': [np.nan, 1, 2],
            'C': [3, 4, 5]
        })
result = test(df0)
assert result.equals(expected), 'Test failed'