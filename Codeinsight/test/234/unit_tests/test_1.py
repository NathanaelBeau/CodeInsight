lst0 = [10, 20, 15]
lst1 = ['ten', 'twenty', 'fifteen']
expected_result0 = tuple([10, 15, 20])
expected_result1 = tuple(['ten', 'fifteen', 'twenty'])
result0, result1 = test(lst0, lst1)
assert result0 == expected_result0 and result1 == expected_result1, 'Test failed'