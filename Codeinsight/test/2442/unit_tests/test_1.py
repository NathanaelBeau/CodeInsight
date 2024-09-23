lst0 = [{'key': {'subkey': 10}}, {'key': {'subkey': 1}}, {'key': {'subkey': 3}}]
expected_output = [{'key': {'subkey': 10}}, {'key': {'subkey': 3}}, {'key': {'subkey': 1}}]
assert test(lst0) == expected_output, 'Test failed'