df0 = pd.DataFrame({ 'A': ['apple', 'banana', 'apple', 'banana'], 'B': [1, 2, 3, 4], 'C': [10, 20, 30, 40] })
var0 = 'A'
var1 = 'B'
expected_result_1 = df0.loc[[2, 3]].reset_index(drop=True)
result1 = test(df0, var0, var1)
assert (result1.values==expected_result_1.values).all(), 'Test failed'