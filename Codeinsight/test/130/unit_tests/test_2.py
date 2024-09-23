data = {'C': [100, 200, 300], 'D': [400, 500, 600]}
df0 = pd.DataFrame(data)
expected_data = {'C': [100, 200, 300], 'D': [400, 500, 600]}
expected_output = pd.DataFrame(expected_data)
assert test(df0) .equals(expected_output), 'Test failed'