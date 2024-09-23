df = pd.DataFrame({
            'A': [1, 2, 3],
            'B': [4, 5, 6]
        })
result = test(df)
expected = pd.RangeIndex(start=0, stop=3, step=1)
assert result .equals(expected), 'Test failed'