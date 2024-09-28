df0 = pd.DataFrame({'X': [30, 10, 20], 'Y': [60, 40, 50]}, index=[2, 0, 1])
expected_result =  pd.DataFrame({'X': [10, 20, 30], 'Y': [40, 50, 60]}, index=[0, 1, 2])
result = test(df0)
assert result.equals(expected_result), 'Test failed'