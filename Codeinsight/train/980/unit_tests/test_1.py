lst0 = [('apple', 5), ('banana', 3), ('cherry', 7)]
expected_result =  [('cherry', 7), ('apple', 5), ('banana', 3)]
result = test(lst0)
assert result == expected_result, 'Test failed'