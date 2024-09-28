df0 = pd.DataFrame({'A': [1, 2, 3], 'B': ['a', 'b', 'c']})
expected_output = [{'A': 1, 'B': 'a'}, {'A': 2, 'B': 'b'}, {'A': 3, 'B': 'c'}]
assert test(df0) ==expected_output, 'Test failed'