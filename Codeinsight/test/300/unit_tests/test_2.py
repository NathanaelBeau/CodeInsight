# Test 2
df0 = pd.DataFrame({"B": ["hello&", "world!", "python$%"]})
col_name = "B"
expected_result =  pd.DataFrame({"B": ["hello", "world", "python"]})
assert test(df0, col_name).equals(expected_result), 'Test failed'