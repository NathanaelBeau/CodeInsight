data = {
            'A': [1, 2, 3],
            'B': [4, 5, 6],
            'A_duplicated': [7, 8, 9]  # Different column name to prevent overwriting
        }
df = pd.DataFrame(data)
df.columns = ['A', 'B', 'A']  # Manually duplicate the column names
result = test(df)
expected = pd.DataFrame({'A': [8, 10, 12], 'B': [4, 5, 6]})
assert result.equals(expected), 'Test failed'