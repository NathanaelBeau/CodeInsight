# Test 1
df0 = pd.DataFrame({ "category": ["A", "A", "B", "B", "C", "C"], "value": [10, 15, 20, 25, 30, 35] })
col_name = "category"
expected_result =  pd.DataFrame({ ('value', 'count'): [2, 2, 2], ('value', 'mean'): [12.5, 22.5, 32.5], ('value', 'sum'): [25, 45, 65], ('value', 'min'): [10, 20, 30], ('value', 'max'): [15, 25, 35] }, index=["A", "B", "C"])
result = test(df0, col_name)
assert result.equals(expected_result), 'Test failed'