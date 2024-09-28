df0 = pd.DataFrame({'X_name': [1, 2, 3], 'Y_name': [4, 5, 6], 'X_age': [7, 8, 9]})
expected_result =  pd.DataFrame({'X_name': [1, 2, 3], 'X_age': [7, 8, 9]})
result = test(df0)
assert result.equals(expected_result), 'Test failed'