lst0 = ['apple', 'banana', 'cherry']
lst1 = ['apple', 'banana', 'berry']
expected_result =  [True, True, False]
assert test(lst0, lst1) == expected_result, 'Test failed'