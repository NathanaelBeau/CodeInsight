df = pd.DataFrame({
            'A': [1, 2, 2, 4],
            'B': ['x', 'y', 'y', 'z'],
            'C': [10, 20, 30, 40]
        })
result = test(df, 'B', 'y', ['A', 'C'])
expected = pd.DataFrame({
            'A': [2, 2],
            'C': [20, 30]
        })
assert result.equals(expected), 'Test failed'