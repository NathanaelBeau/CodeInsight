df0 = pd.DataFrame({
            'A': [1, 2, 3],
            'B': [4, 5, 6]
        })
df1 = pd.DataFrame({
            'A': [1, 1, 1],
            'B': [1, 1, 1]
        })
result = test(df0, df1)
expected = pd.DataFrame({
            'A': [0, 1, 2],
            'B': [3, 4, 5]
        })
assert result.equals(expected), 'Test failed'