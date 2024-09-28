# Unit Test 1
df0 = pd.DataFrame({ 'A': list(range(10)), 'B': list(range(10, 20)) })
train, test = test(df0, frac0=0.7, random_state0=42)
assert len(train) == 7 and len(test) == 3, 'Test failed'