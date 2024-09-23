df = pd.DataFrame({
            'A': [1, 5, 3],
            'B': [4, 2, 6],
            'C': [7, 8, 1]
        })
columns = ['A', 'B', 'C']
result = test(df, columns)
expected = pd.Series([7, 8, 6])
assert result.equals(expected), 'Test failed'