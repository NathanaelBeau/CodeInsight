lst0 = [1, 1]
lst1 = ['a', 'a']
result = test(lst0, lst1)
expected = list(itertools.product(lst0, lst1))
assert result== expected, 'Test failed'