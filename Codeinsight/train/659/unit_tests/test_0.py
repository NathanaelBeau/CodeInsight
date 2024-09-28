# Test 1
df0 = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})
index = 1
col_name = "A"
value = 10
expected_result =  pd.DataFrame({"A": [1, 10, 3], "B": [4, 5, 6]})
result = test(df0, index, col_name, value)
assert result.equals(expected_result), 'Test failed'