df0 = pd.DataFrame({'X': [10, 20, 30, 40], 'Y': [50, 60, 70, 80]})
n0 = 3
expected_result1 = pd.DataFrame({'X': [10, 20, 30], 'Y': [50, 60, 70]})
expected_result2 = pd.DataFrame({'X': [40], 'Y': [80]})
result1, result2 = test(df0, n0)
assert result1.reset_index(drop=True).equals(expected_result1) and result2.reset_index(drop=True).equals(expected_result2), 'Test failed'