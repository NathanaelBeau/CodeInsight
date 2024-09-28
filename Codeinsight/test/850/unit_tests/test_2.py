# Unit Test 2
df0 = pd.DataFrame({ 'X': list(range(20)), 'Y': list(range(20, 40)) })
train, test = test(df0, frac0=0.8, random_state0=1)
assert len(train) == 16 and len(test) == 4, 'Test failed'