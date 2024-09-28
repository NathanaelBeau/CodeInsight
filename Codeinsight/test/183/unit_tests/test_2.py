df0 = pd.DataFrame({ "Name": ["John", "Alice", "John", "Bob"], "City": ["Paris", "New York", "Paris", "London"] })
# Définition de la valeur attendue expected_output
expected_output = pd.DataFrame({ "Name": ["Alice", "Bob", "John"], "City": ["New York", "London", "Paris"], "count": [1, 1, 2] })
assert test(df0) .equals(expected_output), 'Test failed'