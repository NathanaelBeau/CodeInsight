# Test 1
lst0 = [('apple', 3), ('banana', 2), ('cherry', 1)]
lst1 = ['cherry', 'banana', 'apple']
expected_result =  [('cherry', 1), ('banana', 2), ('apple', 3)]
result = test(lst0, lst1)
assert result == expected_result, 'Test failed'