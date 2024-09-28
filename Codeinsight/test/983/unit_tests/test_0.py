# Unit Test 1
lst0 = pd.Series([1, 2, 3, 2, 4, 3])
expected_result =  [2, 3]
result = test(lst0)
assert result == expected_result, 'Test failed'