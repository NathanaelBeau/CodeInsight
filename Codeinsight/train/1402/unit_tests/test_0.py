df2 = pd.DataFrame({
        'animals': ['dog', 'cat', 'dog', 'fish', 'cat']
    })
assert test(df2, 'animals', 'lion') == 0, 'Failed test'