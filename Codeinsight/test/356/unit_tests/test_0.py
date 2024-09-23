lst0 = [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}, {"id": 3, "name": "Charlie"}]
key0 = "name"
value0 = "Bob"
expected_result =  {"id": 2, "name": "Bob"}
result = test(lst0, key0, value0)
assert result == expected_result, 'Test failed'