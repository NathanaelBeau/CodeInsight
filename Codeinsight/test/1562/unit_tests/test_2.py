y_true3 = [1, 1, 1, 1, 0, 0]  # Added negative samples
y_pred3 = [0, 0, 0, 0, 0, 0]
expected_output3 = (2, 0, 4, 0)
assert test(y_true3, y_pred3) == expected_output3, 'Test failed'