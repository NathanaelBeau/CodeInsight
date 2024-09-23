data0 = list(range(20))
train_size0 = 0.5
val_size0 = 0.3
train, val, test = test(data0, train_size0, val_size0)
assert len(train) == 10 and len(val) == 6 and len(test) == 4, 'Test failed'