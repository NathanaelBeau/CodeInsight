# Test 1
df0 = pd.DataFrame({"A": [1, 2, 3]}, index=["a", "b", "c"])
expected_result =  pd.DataFrame({"index": ["a", "b", "c"], "A": [1, 2, 3]})
result = test(df0)
assert result.equals(expected_result), 'Test failed'