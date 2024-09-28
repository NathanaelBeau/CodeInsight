df = pd.DataFrame({
            'Category': ['A', 'A', 'A'],
            'Values': [10, 20, 30]
        })
result = test(df, 'Category', 'Values')
expected = pd.DataFrame({
            'Category': ['A'],
            'Values': [60]
        })
assert result.equals(expected), 'Test failed'