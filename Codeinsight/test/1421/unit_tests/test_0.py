np.random.seed(42)
df0 = pd.DataFrame({ "date"    :  [pd.Timestamp(2012, x, 1) for x in range(1, 11)], "returns" :  0.05 * np.random.randn(10), "dummy"   :  np.repeat(1, 10) })
    # Define expected output
expected_output = pd.DataFrame({ "Mean"    : [df0['returns'].mean()], "Sum"     : [df0['returns'].sum()] }, index=[1])
assert test(df0) .equals(expected_output), 'Test failed'