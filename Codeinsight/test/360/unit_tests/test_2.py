df0 = pd.DataFrame({
            'A': [1, 1, 1],
            'B': [4, 4, 4]
        })
expected = df0.iloc[0:1].reset_index(drop=True)
result = test(df0)
assert result.equals(expected), 'Test failed'