df0 = pd.DataFrame({'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [25, 30, 35]})
column = 'City'
value = ['New York', 'London', 'Paris']
expected_output = pd.DataFrame({'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [25, 30, 35], 'City': ['New York', 'London', 'Paris']})
result = test(df0.copy(), column, value)
assert result.equals(expected_output), 'Test failed'