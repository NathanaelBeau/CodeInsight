# Test 3
df0 = pd.DataFrame({"x": ["apple", "banana", "cherry"], "y": [10, 20, 30]})
index = 2
col_name = "y"
value = 40
expected_result =  pd.DataFrame({"x": ["apple", "banana", "cherry"], "y": [10, 20, 40]})
result = test(df0, index, col_name, value)
assert result.equals(expected_result), 'Test failed'