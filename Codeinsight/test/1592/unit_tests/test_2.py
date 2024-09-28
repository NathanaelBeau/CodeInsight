str0 = "{'a': {'b': {'c': {'d': {'e': {'f': 'final_value'}}}}}}"
expected_output = {'a': {'b': {'c': {'d': {'e': {'f': 'final_value'}}}}}}
assert test(str0) ==expected_output, 'Test failed'