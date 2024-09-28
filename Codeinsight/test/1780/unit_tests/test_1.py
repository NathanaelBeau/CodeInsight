# Test 1: Using 'in' operation
df0 = pd.DataFrame({"A": [1, 2, 3, 4], "B": ["a", "b", "c", "d"]})
col_name = "A"
values = [1, 3]
operation = "in"
expected_result =  pd.DataFrame({"A": [1, 3], "B": ["a", "c"]}).reset_index(drop=True)
result = test(df0, col_name, values, operation).reset_index(drop=True)
assert result.equals(expected_result), 'Test failed'