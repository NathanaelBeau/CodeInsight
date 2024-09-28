lst0 = [3.14, 2.71, 1.41, 0.5]
lst1 = [1.5, 1.0, 0.5, 0.1]
expected_result =  [1.6400000000000001, 1.71, 0.9099999999999999, 0.4]
result = test(lst0, lst1)
assert result == expected_result, 'Test failed'