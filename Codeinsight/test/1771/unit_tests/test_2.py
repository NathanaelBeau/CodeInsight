lst0 = [{'key': {'subkey': 7}}, {'key': {'subkey': 4}}, {'key': {'subkey': 6}}]
expected_output = [{'key': {'subkey': 7}}, {'key': {'subkey': 6}}, {'key': {'subkey': 4}}]
assert test(lst0) == expected_output, 'Test failed'