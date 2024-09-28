df_data = {'Mt': ['A', 'A', 'B', 'B', 'C'],
           'Value': [10, 20, 30, 40, 50]}
df0 = pd.DataFrame(df_data)
var0 = 'Mt'
expected_output = df0.groupby(var0, as_index=False).first()
assert test(df0, var0).equals(expected_output), 'Test failed'