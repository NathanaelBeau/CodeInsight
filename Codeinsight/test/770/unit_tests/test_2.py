lst0 = [{'other_key': 'x'}, {'another_key': 'y'}, {'yet_another_key': 'z'}]
expected_result =  []
result = test(lst0)
assert result == expected_result, 'Test failed'