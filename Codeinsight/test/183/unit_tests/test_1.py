df0 = pd.DataFrame({ "Name": ["Alice", "Bob"], "City": ["New York", "London"] })
expected_output = pd.DataFrame({ "Name": ["Alice", "Bob"], "City": ["New York", "London"], "count": [1, 1] })
assert test(df0) .equals(expected_output), 'Test failed'