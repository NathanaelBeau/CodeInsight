# Test 3
df0 = pd.DataFrame({"x": ["apple", "banana", "cherry", "date"], "y": [10, 20, 30, 40]})
col_name = "x"
value = "banana"
expected_result_3 = pd.DataFrame({"x": ["apple", "cherry", "date"], "y": [10, 30, 40]})
result_3 = test(df0, col_name, value).reset_index(drop=True)
assert result_3.equals(expected_result_3), 'Test failed'