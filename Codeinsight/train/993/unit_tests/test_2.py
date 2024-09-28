lst0 = [(1, 'one'), (2, 'two'), (3, 'three')]
expected_result =  {1: 'one', 2: 'two', 3: 'three'}
result = test(lst0)
assert result == expected_result, 'Test failed'