df0 = pd.DataFrame({'X': [10, 20, 30, 40], 'Y': [50, 60, 70, 80]}, index=[0, 1, 2, 3])
lst0 = [1, 3]
expected_result =  pd.DataFrame({'X': [20, 40], 'Y': [60, 80]}, index=[1, 3])
result = test(df0, lst0)
assert result.equals(expected_result), 'Test failed'