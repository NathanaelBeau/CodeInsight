dict0 = { 'key1': { 'subkey1': 1, 'subkey2': 2 }, 'key2': { 'subkey3': 3, 'subkey4': 4 } }
expected_output = 6
assert test(dict0) ==expected_output, 'Test failed'