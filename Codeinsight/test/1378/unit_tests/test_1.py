df0 = pd.DataFrame({ 'ID': [101, 102], 'City': ['New York', 'Los Angeles'], 'Population': [8623457, 3990456] })
lst0 = ['City', 'ID']
expected_output = (test(df0, lst0))
assert test(df0, lst0).equals(expected_output), 'Test failed'