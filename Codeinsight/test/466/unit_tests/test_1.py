df0 = pd.DataFrame({'M': [17, 18], 'N': [19, 20], 'O': [21, 22]})
start_column0, end_column0 = 'M', 'N'
expected_result =  pd.DataFrame({'M': [17, 18], 'N': [19, 20]})
result = test(df0.copy(), start_column0, end_column0)
assert result.equals(expected_result), 'Test failed'