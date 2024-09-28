df0 = pd.DataFrame({'ID': [1, 2, 3], 'Name': ['Alice', 'Bob', 'Charlie']})
df1 = pd.DataFrame({'Age': [25, 30, 35], 'City': ['New York', 'London', 'Paris']})
expected_output = pd.DataFrame({'ID': [1, 2, 3], 'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [25, 30, 35], 'City': ['New York', 'London', 'Paris']})
assert test(df0, df1) .equals(expected_output), 'Test failed'