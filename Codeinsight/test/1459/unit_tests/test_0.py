df = pd.DataFrame({
            'A': [1, 2, 3],
            'B': [4, 5, 6],
            'C': [7, 8, 9]
        })
columns = ['A', 'B']
result = test(df, columns)
expected = pd.Series([4, 5, 6])
assert result.equals(expected), 'Test failed'