# Test 2
df0 = pd.DataFrame({"name": ["Alice", "Bob", "Charlie"], "age": [25, 30, 35]})
index = 0
col_name = "name"
value = "Alex"
expected_result =  pd.DataFrame({"name": ["Alex", "Bob", "Charlie"], "age": [25, 30, 35]})
result = test(df0, index, col_name, value)
assert result.equals(expected_result), 'Test failed'