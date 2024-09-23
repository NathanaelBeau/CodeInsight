# Test 3
df0 = pd.DataFrame({"C": ["apple", "banana", "cherry"]}, index=["x", "y", "z"])
expected_result =  pd.DataFrame({"index": ["x", "y", "z"], "C": ["apple", "banana", "cherry"]})
result = test(df0)
assert result.equals(expected_result), 'Test failed'