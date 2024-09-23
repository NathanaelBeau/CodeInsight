# Test 3: Using 'in' operation
df0 = pd.DataFrame({"x": ["apple", "banana", "cherry", "date"], "y": [10, 20, 30, 40]})
col_name = "x"
values = ["apple", "date"]
operation = "in"
expected_result =  pd.DataFrame({"x": ["apple", "date"], "y": [10, 40]}).reset_index(drop=True)
result = test(df0, col_name, values, operation).reset_index(drop=True)
assert result.equals(expected_result), 'Test failed'