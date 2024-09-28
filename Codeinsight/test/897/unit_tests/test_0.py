s1 = ".*?^$|+()[]{}"
expected_output1 = "\.\*\?\^\$\|\+\(\)\[\]\{\}"
assert test(s1) == expected_output1, 'Test failed'