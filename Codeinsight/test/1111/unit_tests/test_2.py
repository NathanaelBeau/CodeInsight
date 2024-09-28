df = pd.DataFrame({
            'text': ['-world', '-bar', '-text']
        })
result = test(df, 'text', 'part1', 'part2', '-')
expected = pd.DataFrame({
            'text': ['-world', '-bar', '-text'],
            'part1': ['', '', ''],
            'part2': ['world', 'bar', 'text']
        })
assert result.equals(expected), 'Test failed'