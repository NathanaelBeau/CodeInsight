# Test 1
df0 = pd.DataFrame({ "category": ["A", "A", "B", "B", "C", "C"], "value": [10, 15, 20, 25, 30, 35] })
col_name = "category"
agg_function = "sum"
expected_result =  pd.DataFrame({ "category": ["A", "B", "C"], "value": [25, 45, 65] })
result = test(df0, col_name, agg_function)
assert result.equals(expected_result), 'Test failed'