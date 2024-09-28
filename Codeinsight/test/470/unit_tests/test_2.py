lst0 = [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}, {"id": 3, "name": "Charlie"}]
key0 = "id"
value0 = 4
expected_result =  None
result = test(lst0, key0, value0)
assert result == expected_result, 'Test failed'