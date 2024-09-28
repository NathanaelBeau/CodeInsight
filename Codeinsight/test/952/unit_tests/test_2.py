dict0 = {'dog': 'bark', 'cat': 'meow', 'cow': 'moo'}
dict1 = {'bark': 'sound', 'meow': 'sound', 'moo': 'sound'}
expected_output = {'dog': 'sound', 'cat': 'sound', 'cow': 'sound'}
assert test(dict0, dict1) ==expected_output, 'Test failed'