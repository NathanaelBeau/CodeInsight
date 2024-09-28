arg = pd.DataFrame({'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [25, 30, 35]})
expected_output = pd.Series({'Name': 'object', 'Age': 'int64'})
assert test(arg).equals(expected_output), 'Test failed'