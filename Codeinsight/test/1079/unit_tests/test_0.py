# Test 1
lst0 = [{"A": 1, "B": 2}, {"A": 3, "B": 4}]
expected_result =  pd.DataFrame({"A": [1, 3], "B": [2, 4]})
result = test(lst0)
assert result.equals(expected_result), 'Test failed'