lst0 = pd.Series(['a', 'b', 'c', 'a', 'd', 'e', 'e'])
expected_result =  ['a', 'e']
result = test(lst0)
assert result == expected_result, 'Test failed'