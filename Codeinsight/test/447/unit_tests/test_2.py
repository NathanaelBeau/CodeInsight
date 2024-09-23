lst0= [10, 20, 30, 40]
lst1= ['abc', 'def', 'ghi', 'jkl']
expected_output = [(10, 'abc'), (20, 'def'), (30, 'ghi'), (40, 'jkl')]
assert test(lst0, lst1) == expected_output, 'Test failed'