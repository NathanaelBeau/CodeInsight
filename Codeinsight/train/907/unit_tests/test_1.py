df0 = pd.DataFrame({
            'A': [1, 2, 3],
            'B': [4, 5, 6]
        })
result = test(df0)
expected = df0
assert result.equals(expected), 'Test failed'