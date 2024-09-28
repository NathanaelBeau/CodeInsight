lst0 = [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}, {"id": 3, "name": "Charlie"}]
key0 = "id"
value0 = 1
expected_result =  {"id": 1, "name": "Alice"}
result = test(lst0, key0, value0)
assert result == expected_result, 'Test failed'