# Test 1
df0_1 = pd.DataFrame({'A': [10, 20, 30, 40], 'B': [50, 60, 70, 80]})
idx_1 = 2
expected_result_1 = pd.Series({'A': 30, 'B': 70}, name=idx_1)
result_1 = test(df0_1, idx_1)
assert result_1.equals(expected_result_1), 'Test failed'