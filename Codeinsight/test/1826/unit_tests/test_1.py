# Unit Test 3
df0 = pd.DataFrame({ 'P': list(range(5)), 'Q': list(range(5, 10)) })
train, test = test(df0, frac0=0.6)
assert len(train) == 3 and len(test) == 2, 'Test failed'