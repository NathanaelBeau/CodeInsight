# Test 3
lst0 = [{"x": 10, "y": 20}, {"x": 30, "y": 40}, {"x": 50, "y": 60}]
expected_result =  pd.DataFrame({"x": [10, 30, 50], "y": [20, 40, 60]})
result = test(lst0)
assert result.equals(expected_result), 'Test failed'