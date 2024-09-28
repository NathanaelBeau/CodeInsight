df0 = pd.DataFrame({ 'Username': ['user1', 'user2'], 'Name': ['John', 'Jane'], 'Age': [25, 30] })
lst0 = ['Username', 'Name']
expected_output = (test(df0, lst0))
assert test(df0, lst0).equals(expected_output), 'Test failed'