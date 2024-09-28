df = pd.DataFrame({
            'A': [1, 5, 3],
            'B': [4, 2, 6],
            'C': [7, 8, 1]
        })
columns = []
result = test(df, columns)
expected = pd.Series([np.NaN] * len(df))
assert result.equals(expected), 'Test failed'