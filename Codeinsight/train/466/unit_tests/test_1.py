data = {'X': [10, 20, 30], 'Y': [40, 50, 60]}
df0 = pd.DataFrame(data)
expected_data = {'X': [10, 20, 30], 'Y': [40, 50, 60]}
expected_output = pd.DataFrame(expected_data)
assert test(df0) .equals(expected_output), 'Test failed'