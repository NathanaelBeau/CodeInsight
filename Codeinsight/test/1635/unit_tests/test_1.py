lst0 = [1, 2]
lst1 = []
result = test(lst0, lst1)
expected = list(itertools.product(lst0, lst1))
assert result== expected, 'Test failed'