data = {
            'A': [1, 2, 3, 4],
            'B': [10, 20, 30, 40],
            'C': [5, 15, 25, 35]
        }
df = pd.DataFrame(data)
result = test(df, 'df0["A"] > 2')
expected = pd.DataFrame({
            'A': [3, 4],
            'B': [30, 40],
            'C': [25, 35]
        }, index=[2, 3])
assert result.equals(expected), 'Test failed'