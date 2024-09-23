lst0 = [(1, 'a'), (2, 'b'), (3, 'c')]
lst1 = [(1, 'z'), (4, 'y')]
expected_result =  [(1, 'a')]
assert test(lst0, lst1) == expected_result, 'Test failed'