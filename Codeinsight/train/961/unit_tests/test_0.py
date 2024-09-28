# Test 1
df0 = pd.DataFrame({"A": [1, 2, 3, 4], "B": [10, 20, 30, 40]})
col_name = "A"
value = 3
expected_result =  pd.DataFrame({"A": [1, 2, 4], "B": [10, 20, 40]})
result = test(df0, col_name, value).reset_index(drop=True)
assert result.equals(expected_result), 'Test failed'