df0 = pd.DataFrame({ 'A': ['foo', 'bar', 'baz', 'foo', 'bar', 'baz'], 'B': [1, 2, 3, 4, 5, 6] })
expected_result =  pd.DataFrame({ ('B', 'sum'): {'bar': 7, 'baz': 9, 'foo': 5}, ('B', 'count'): {'bar': 2, 'baz': 2, 'foo': 2} })
result = test(df0)
assert result.equals(expected_result), 'Test failed'