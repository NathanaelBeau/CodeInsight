X0 = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]]
y0 = [1, 0, 1, 0, 1, 0]
var0 = 0.5
var1 = 0
X_train, X_test, y_train, y_test = test(X0, y0, var0, var1)
assert len(X_train) == 3 and len(X_test) == 3, 'Test failed'