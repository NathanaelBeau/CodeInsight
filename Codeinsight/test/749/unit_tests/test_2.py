df0 = pd.DataFrame({ 'E': [100, 200, 300], 'F': [400, 500, 600] })
expected_output = df0  # No duplicate indices, so the dataframe remains unchanged
assert test(df0).equals(expected_output), 'Test failed'