y_true2 = [0, 0, 0, 0, 1, 1]  # Added positive samples
y_pred2 = [0, 0, 0, 0, 1, 1]
expected_output2 = (4, 0, 0, 2)
assert test(y_true2, y_pred2) == expected_output2, 'Test failed'