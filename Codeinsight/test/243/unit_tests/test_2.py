lst0 = [(10, 'j'), (11, 'k')]
lst1 = [(10, 'l'), (11, 'm')]
expected_result =  [(10, 'j'), (11, 'k')]
assert test(lst0, lst1) == expected_result, 'Test failed'