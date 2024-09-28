data = {
            'A': [1, 2, 3, 4],
            'B': [10, 20, 30, 40],
            'C': [5, 15, 25, 35]
        }
df = pd.DataFrame(data)
result = test(df, '(df0["A"] > 1) & (df0["B"] < 40)')
expected = pd.DataFrame({
            'A': [2, 3],
            'B': [20, 30],
            'C': [15, 25]
        }, index=[1, 2])
assert result.equals(expected), 'Test failed'