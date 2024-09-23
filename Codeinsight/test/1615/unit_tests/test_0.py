data = {'name': ['John', 'Alice', 'Bob'], 'age': [25, 30, 35]}
df0 = pd.DataFrame(data)
df0.set_index('name', inplace=True)
expected_output = ['John', 'Alice', 'Bob']
assert test(df0) == expected_output, 'Test failed'