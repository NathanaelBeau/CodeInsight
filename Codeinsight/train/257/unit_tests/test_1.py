# Test 2
df0 = pd.DataFrame({ "group": ["X", "X", "Y", "Y", "Z", "Z"], "score": [50, 60, 70, 80, 90, 100] })
col_name = "group"
expected_result =  pd.DataFrame({ ('score', 'count'): [2, 2, 2], ('score', 'mean'): [55.0, 75.0, 95.0], ('score', 'sum'): [110, 150, 190], ('score', 'min'): [50, 70, 90], ('score', 'max'): [60, 80, 100] }, index=["X", "Y", "Z"])
result = test(df0, col_name)
assert result.equals(expected_result), 'Test failed'