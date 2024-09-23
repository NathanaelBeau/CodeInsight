df = pd.DataFrame({
            'Category': ['A', 'A', 'B', 'B', 'C'],
            'Values': [10, 20, 10, 30, 50]
        })
result = test(df, 'Category', 'Values')
expected = pd.DataFrame({
            'Category': ['A', 'B', 'C'],
            'Values': [30, 40, 50]
        })
assert result.equals(expected), 'Test failed'