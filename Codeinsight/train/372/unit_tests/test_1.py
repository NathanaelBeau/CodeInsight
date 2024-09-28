df_data = {'Category': ['X', 'X', 'Y', 'Y', 'Z'],
           'Score': [90, 85, 70, 75, 60]}
df0 = pd.DataFrame(df_data)
var0 = 'Category'
expected_output = df0.groupby(var0, as_index=False).first()
assert test(df0, var0).equals(expected_output), 'Test failed'