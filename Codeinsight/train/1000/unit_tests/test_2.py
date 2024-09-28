df = pd.DataFrame({
            'A': [0.1, 0.25, 0.3],
            'B': [0.2, 0.35, 0.45],
            'C': [1, 2, 3]
        })
columns = []
result = test(df, columns)
expected = df.copy()  # No columns should be changed
assert result.equals(expected), 'Test failed'