lst0 = [3, 1, 2]
lst1 = ['three', 'one', 'two']
expected_result0 = tuple([1, 2, 3])
expected_result1 = tuple(['one', 'two', 'three'])
result0, result1 = test(lst0, lst1)
assert result0 == expected_result0 and result1 == expected_result1, 'Test failed'