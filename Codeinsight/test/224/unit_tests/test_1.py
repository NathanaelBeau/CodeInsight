df0 = pd.DataFrame({'Name': ['John', 'Emma', 'Alice'], 'Age': [25, 30, 35]})
expected_output = [{'Name': 'John', 'Age': 25}, {'Name': 'Emma', 'Age': 30}, {'Name': 'Alice', 'Age': 35}]
assert test(df0) ==expected_output, 'Test failed'