df_data = {'Group': ['G1', 'G1', 'G2', 'G2', 'G3'],
           'Count': [100, 150, 80, 120, 200]}
df0 = pd.DataFrame(df_data)
var0 = 'Group'
expected_output = df0.groupby(var0, as_index=False).first()
assert test(df0, var0).equals(expected_output), 'Test failed'