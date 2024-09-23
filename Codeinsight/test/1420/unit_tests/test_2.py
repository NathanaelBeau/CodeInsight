# Test 3
df0_1 = pd.DataFrame({'A': [10, 20, 30, 40], 'B': [50, 60, 70, 80]})
idx_3 = 3
expected_result_3 = pd.Series({'A': 40, 'B': 80}, name=idx_3)
result_3 = test(df0_1, idx_3)
assert result_3.equals(expected_result_3), 'Test failed'