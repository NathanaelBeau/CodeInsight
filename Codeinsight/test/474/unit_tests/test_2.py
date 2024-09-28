var0 = pd.DataFrame({'Category': ['A', 'B', 'A', 'B'], 'Count': [5, 6, 7, 8]})
col0 = 'Category'
col1 = 'Count'
expected_result =  pd.DataFrame({'Category': ['A', 'B'], 'Count': [12, 14]})
result = test(var0, col0, col1)
assert result.equals(expected_result), 'Test failed'