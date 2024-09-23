df0 = pd.DataFrame({ "Name": ["John", "Alice", "John", "Bob", "Alice"], "City": ["Paris", "New York", "Paris", "London", "New York"] })
expected_output = pd.DataFrame({ "Name": ["Alice", "Bob", "John"], "City": ["New York", "London", "Paris"], "count": [2, 1, 2] })
assert test(df0) .equals(expected_output), 'Test failed'