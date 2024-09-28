lst0 = [{"values": 1, "other_key": 2}, {"values": 3}, {"yet_another_key": 4}]
expected_result =  [1, 3]
result = test(lst0)
assert result == expected_result, 'Test failed'