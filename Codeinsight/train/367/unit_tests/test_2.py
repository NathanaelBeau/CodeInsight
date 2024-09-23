a = [1, 2]
b = a
lst0 = [a]
lst1 = [b]
expected_result =  [True]
assert test(lst0, lst1) == expected_result, 'Test failed'