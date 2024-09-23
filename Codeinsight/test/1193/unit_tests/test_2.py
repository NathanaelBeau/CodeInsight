# Test 2
lst0 = [('dog', 'a'), ('cat', 'b'), ('bird', 'c')]
lst1 = ['bird', 'dog', 'cat']
expected_result =  [('bird', 'c'), ('dog', 'a'), ('cat', 'b')]
result = test(lst0, lst1)
assert result == expected_result, 'Test failed'