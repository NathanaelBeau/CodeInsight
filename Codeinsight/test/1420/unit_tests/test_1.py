# Test 2
df0_1 = pd.DataFrame({'A': [10, 20, 30, 40], 'B': [50, 60, 70, 80]})
idx_2 = 0
expected_result_2 = pd.Series({'A': 10, 'B': 50}, name=idx_2)
result_2 = test(df0_1, idx_2)
assert result_2.equals(expected_result_2), 'Test failed'