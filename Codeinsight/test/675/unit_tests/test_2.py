df0 = pd.DataFrame({'M': [1, 2], 'N': [3, 4]})
n0 = 1
expected_result1 = pd.DataFrame({'M': [1], 'N': [3]})
expected_result2 = pd.DataFrame({'M': [2], 'N': [4]})
result1, result2 = test(df0, n0)
assert result1.reset_index(drop=True).equals(expected_result1) and result2.reset_index(drop=True).equals(expected_result2), 'Test failed'