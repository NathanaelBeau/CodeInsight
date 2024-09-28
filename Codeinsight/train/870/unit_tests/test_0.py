df0 = pd.DataFrame({"A": ["a", "b"], "B": ["c", "d"]})
expected_result =  pd.Series(["a c", "b d"])
result = test(df0)
assert result.equals(expected_result), 'Test failed'