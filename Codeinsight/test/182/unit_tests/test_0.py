data0 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
train_size0 = 0.6
val_size0 = 0.2
train, val, test = test(data0, train_size0, val_size0)
assert len(train) == 6 and len(val) == 2 and len(test) == 2, 'Test failed'