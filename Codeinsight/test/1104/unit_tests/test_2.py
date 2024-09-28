X0 = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12], [13, 14]]
y0 = [1, 0, 1, 0, 1, 0, 1]
var0 = 0.3
var1 = 123
X_train, X_test, y_train, y_test = test(X0, y0, var0, var1)
assert len(X_train) == 4 and len(X_test) == 3, 'Test failed'