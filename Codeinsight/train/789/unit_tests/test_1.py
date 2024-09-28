lst0 = ['cat', 'dog', 'elephant', 'bird']
lst1 = [4, 1, 3, 2]
expected_result =  ['dog', 'bird', 'elephant', 'cat']
result = test(lst0, lst1)
assert result == expected_result, 'Test failed'