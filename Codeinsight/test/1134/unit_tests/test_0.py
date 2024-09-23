# Test 2: Using 'not in' operation
df0 = pd.DataFrame({"name": ["Alice", "Bob", "Charlie", "David"], "age": [25, 30, 35, 40]})
col_name = "name"
values = ["Alice", "David"]
operation = "not in"
expected_result =  pd.DataFrame({"name": ["Bob", "Charlie"], "age": [30, 35]}).reset_index(drop=True)
result = test(df0, col_name, values, operation).reset_index(drop=True)
assert result.equals(expected_result), 'Test failed'