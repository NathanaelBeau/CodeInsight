y_true1 = [0, 1, 0, 1, 0, 1]  # Added more samples for balance
y_pred1 = [0, 1, 1, 0, 0, 1]
expected_output1 = (2, 1, 1, 2)
assert test(y_true1, y_pred1) == expected_output1, 'Test failed'