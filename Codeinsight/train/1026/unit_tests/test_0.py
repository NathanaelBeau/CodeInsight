# Test 1
df0 = pd.DataFrame({'A': [1., 2., np.inf, 4.], 'B': [5., 6., 7., 8.]})
var0 = 'A'
expected_result =  pd.DataFrame({'A': [1.0, 2.0, 4.0], 'B': [5., 6., 8.]})
result = test(df0, var0).reset_index(drop=True)
assert result.equals(expected_result), 'Test failed'