# Test 3
df0 = pd.DataFrame({"C": ["test123", "456test", "789"]})
col_name = "C"
expected_result =  pd.DataFrame({"C": ["test123", "456test", "789"]})
assert test(df0, col_name).equals(expected_result), 'Test failed'