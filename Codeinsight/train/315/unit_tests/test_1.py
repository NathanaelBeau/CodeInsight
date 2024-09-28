lst0 = [{"values": "a"}, {"values": "b"}, {"values": "c"}]
expected_result =  ["a", "b", "c"]
result = test(lst0)
assert result == expected_result, 'Test failed'