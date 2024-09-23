df0 = pd.DataFrame({ "group": ["X", "X", "Y", "Y", "Z", "Z"], "score": [50, 60, 70, 80, 90, 100] })
col_name = "group"
agg_function = "mean"
expected_result =  pd.DataFrame({ "group": ["X", "Y", "Z"], "score": [55.0, 75.0, 95.0] })
result = test(df0, col_name, agg_function)
assert result.equals(expected_result), 'Test failed'