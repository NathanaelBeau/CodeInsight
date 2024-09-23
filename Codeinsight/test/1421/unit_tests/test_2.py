np.random.seed(42)
df0 = pd.DataFrame({ "date"    :  [pd.Timestamp(2019, x, 1) for x in range(1, 4)], "returns" :  0.05 * np.random.randn(3), "dummy"   :  np.repeat(4, 3) })
expected_output = pd.DataFrame({ "Mean"    : [df0['returns'].mean()], "Sum"     : [df0['returns'].sum()] }, index=[4])
assert test(df0) .equals( expected_output), 'Test failed'