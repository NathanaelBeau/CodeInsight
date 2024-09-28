lst0 = [{'key': {'subkey': 5}}, {'key': {'subkey': 2}}, {'key': {'subkey': 8}}]
expected_output = [{'key': {'subkey': 8}}, {'key': {'subkey': 5}}, {'key': {'subkey': 2}}]
assert test(lst0) == expected_output, 'Test failed'