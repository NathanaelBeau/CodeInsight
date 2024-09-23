# Test 1
lst0 = ["Hello world", "The quick brown fox", "Pandas are awesome"]
lst1 = ["world", "fox"]
expected_result =  ["Hello", "The quick brown", "Pandas are awesome"]
assert test(lst0, lst1) == expected_result, 'Test failed'