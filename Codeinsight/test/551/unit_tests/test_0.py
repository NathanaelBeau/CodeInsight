df0 = pd.DataFrame({
            'A': [1, 2, 3],
            'B': ['$100.00', '$200.50', '$300.75'],
            'C': ['$10.50', '$20.25', '$30.00']
        })
expected = pd.DataFrame({
            'A': [1, 2, 3],
            'B': [100.00, 200.50, 300.75],
            'C': [10.50, 20.25, 30.00]
        })
result = test(df0)
assert result.equals(expected), 'Test failed'