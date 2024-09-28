arg = pd.DataFrame({'City': ['New York', 'San Francisco', 'Los Angeles'], 'Population': [8000000, 900000, 4000000]})
expected_output = pd.Series({'City': 'object', 'Population': 'int64'})
assert test(arg).equals(expected_output), 'Test failed'