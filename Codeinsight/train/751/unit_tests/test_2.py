lst0 = [True, False]
lst1 = [42, 0]
expected_output = [(True, 42), (False, 0)]
assert test(lst0, lst1) == expected_output, 'Test failed'