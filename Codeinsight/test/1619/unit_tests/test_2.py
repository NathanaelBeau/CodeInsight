str0 = "a=1 b=2 c=3 d=4 e=5"
expected_output = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
assert test(str0) ==expected_output, 'Test failed'