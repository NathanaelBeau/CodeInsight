df0 = pd.DataFrame({
            'A': [0, 0, 0],
            'B': [0, 0, 0]
        })
expected = pd.DataFrame(columns=[], index=[0, 1, 2])
result = test(df0)
assert result.equals(expected), 'Test failed'