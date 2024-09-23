# Test 3
df0 = pd.DataFrame({ "label": ["M", "M", "F", "F", "O", "O"], "points": [5, 6, 7, 8, 9, 10] })
col_name = "label"
agg_function = "max"
expected_result_3 = pd.DataFrame({ "label": ["F", "M", "O"], "points": [8, 6, 10] })
result_3 = test(df0, col_name, agg_function)
assert result_3.equals(expected_result_3), 'Test failed'