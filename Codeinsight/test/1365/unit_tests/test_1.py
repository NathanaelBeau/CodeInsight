df0 = pd.DataFrame({'Name': ['John', 'Emily', 'Michael'], 'Age': [35, 28, 42], 'Country': ['USA', 'Canada', 'UK']})
expected_output = [['Name', 'John', 'Emily', 'Michael'], ['Age', 35, 28, 42], ['Country', 'USA', 'Canada', 'UK']]
assert test(df0)== expected_output, 'Test failed'