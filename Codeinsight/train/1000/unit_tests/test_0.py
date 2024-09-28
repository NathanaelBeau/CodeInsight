df = pd.DataFrame({
            'A': [0.1, 0.25, 0.3],
            'B': [0.2, 0.35, 0.45],
            'C': [1, 2, 3]
        })
columns = ['A', 'B']
result = test(df, columns)
expected = pd.DataFrame({
            'A': ['10.00%', '25.00%', '30.00%'],
            'B': ['20.00%', '35.00%', '45.00%'],
            'C': [1, 2, 3]
        })
assert result.equals(expected), 'Test failed'