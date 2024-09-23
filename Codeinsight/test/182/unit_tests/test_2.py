data0 = list(range(100))
train_size0 = 0.7
val_size0 = 0.15
train, val, test = test(data0, train_size0, val_size0)
assert len(train) == 69 and len(val) == 15 and len(test) == 16, 'Test failed'