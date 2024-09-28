# Test 2
lst0 = [{"name": "Alice", "age": 25}, {"name": "Bob", "age": 30}]
expected_result =  pd.DataFrame({"name": ["Alice", "Bob"], "age": [25, 30]})
result = test(lst0)
assert result.equals(expected_result), 'Test failed'