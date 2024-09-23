lst0 = ['A\tB\tC', '1\t2\t3']
expected_result =  [['A', 'B', 'C'], ['1', '2', '3']]
result = test(lst0)
assert result == expected_result, 'Test failed'