df1 = pd.DataFrame({
            'A': [1, 2, 3],
            'B': ['x', 'y', 'z']
        })
df2 = pd.DataFrame({
            'A': [10, 20, 30],
            'B': ['a', 'b', 'c']
        })
result = test(df1, df2, 'A')
expected = pd.DataFrame({
            'df1': [1, 2, 3],
            'df2': [10, 20, 30]
        })
assert result.equals(expected), 'Test failed'