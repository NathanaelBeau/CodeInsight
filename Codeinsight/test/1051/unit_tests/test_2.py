# Test 2
df0 = pd.DataFrame({"name": ["Alice", "Bob", "Charlie", "David"], "age": [25, 30, 35, 40]})
col_name = "name"
value = "Charlie"
result_2 = test(df0, col_name, value).reset_index(drop=True)
expected_result_2 = pd.DataFrame({"name": ["Alice", "Bob", "David"], "age": [25, 30, 40]})
assert result_2.equals(expected_result_2), 'Test failed'