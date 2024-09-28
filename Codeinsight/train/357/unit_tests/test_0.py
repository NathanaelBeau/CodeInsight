df0 = pd.DataFrame({
            'A': [['a', 'b'], ['c', 'd'], ['e', 'f']],
            'B': ['initial', 'initial', 'initial']
        })
result = test(df0, 'A', 'B')
expected = pd.DataFrame({
            'A': [['a', 'b'], ['c', 'd'], ['e', 'f']],
            'B': ['ab', 'cd', 'ef']
        })

assert result.equals(expected), 'Test failed'